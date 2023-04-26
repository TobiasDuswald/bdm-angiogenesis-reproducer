import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def GetAllJSONFiles(folder):
    """ Finds all JSON files in any subdirectory of folder. Returns list."""
    import os

    data_files = []
    treatment_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".json"):
                if "treatment" in file:
                    treatment_files.append(os.path.join(root, file))
                else:
                    data_files.append(os.path.join(root, file))
    return data_files, treatment_files[0]


def SimplifyDictionary(data):
    # Get the number of time series
    n_time_series = len(data["data_"])

    # Setup data structure
    new_data = {}
    for i in range(n_time_series):
        new_data[data["data_"][i]["first"]] = {
            "x": np.array([]),
            "y": np.array([]),
        }

    # Factor to convert from minutes to days
    minutes_to_days = 1.0 / (60.0 * 24.0)

    # Fill in the data structure
    for i in range(n_time_series):
        new_data[data["data_"][i]["first"]]["x"] = np.array(
            data["data_"][i]["second"]["x_values"]
        ) * minutes_to_days
        new_data[data["data_"][i]["first"]]["y"] = np.array(
            data["data_"][i]["second"]["y_values"]
        )

    return new_data


def ComputeAdditionalTimeSeries(data):
    # Create total cell count
    data["total"] = {
        "x": data["q"]["x"],
        "y": data["q"]["y"]
        + data["sg2"]["y"]
        + data["g1"]["y"]
        + data["d"]["y"]
        + data["h"]["y"],
    }
    # Create living cell counts (all but dead cells)
    data["living"] = {
        "x": data["q"]["x"],
        "y": data["q"]["y"]
        + data["sg2"]["y"]
        + data["g1"]["y"]
        + data["h"]["y"],
    }
    # Create proliferating cell counts (all but dead and quiescent cells)
    data["proliferating"] = {
        "x": data["q"]["x"],
        "y": data["sg2"]["y"] + data["g1"]["y"],
    }

    return data

def AggregateData(data):
    # Get the number of samples
    n_samples = len(data)

    # Get the number of time points
    n_time_points = len(data[0]["q"]["x"])

    # Setup data structure
    aggregated_data = {}
    for key in data[0].keys():
        aggregated_data[key] = {
            "x": np.array([]),
            "y_mean": np.array([]),
            "y_std": np.array([]),
        }

    # Fill in the data structure
    for key in data[0].keys():
        aggregated_data[key]["x"] = data[0][key]["x"]
        tmp = np.zeros((n_samples, n_time_points))
        for i in range(n_samples):
            tmp[i, :] = data[i][key]["y"]
        aggregated_data[key]["y_mean"] = np.mean(tmp, axis=0)
        aggregated_data[key]["y_std"] = np.std(tmp, axis=0)

    return aggregated_data



def PlotSingleTimeSeries(data):
    # Cell count names
    cell_count_names = [
        "q",
        "sg2",
        "g1",
        "d",
        "h",
        "total",
        "living",
        "proliferating",
    ]
    for key in cell_count_names:
        plt.plot(data[key]["x"], data[key]["y"], label=key)
    plt.legend()
    plt.show()

def PlotAggregatedData(data, treatment_plan, folder):
    color_q = "#EDC728"
    color_sg2 = "#1A9C13"
    color_g1 = "#69ED15"
    color_d = "#000000"
    color_h = "#A0A0A0"
    color_living = "#A51313"
    color_proliferating = "#e377c2"
    color_total = "#307EC9"
    color_treatment_tra = "fuchsia"
    color_treatment_rad = "orangered"

    # Plot the treatment plan
    start_tra_1 = treatment_plan["tra_start_1"] / (60.0 * 24.0)
    end_tra_1 = treatment_plan["tra_end_1"]/ (60.0 * 24.0)
    start_tra_2 = treatment_plan["tra_start_2"]/ (60.0 * 24.0)
    end_tra_2 = treatment_plan["tra_end_2"]/ (60.0 * 24.0)
    start_dox = treatment_plan["dox_start"]/ (60.0 * 24.0)
    end_dox = treatment_plan["dox_end"]/ (60.0 * 24.0)

    # Set the figure size
    plt.figure(figsize=(5, 3))

    # Plot the treatment plan
    plt.axvspan(start_tra_1, end_tra_1, color=color_treatment_tra, alpha=0.2, label="TRA")
    plt.axvspan(start_tra_2, end_tra_2, color=color_treatment_tra, alpha=0.2)
    plt.axvspan(start_dox, end_dox, color=color_treatment_rad, alpha=0.2, label="DOX")

    # Plot the Q data
    plt.plot(
        data["q"]["x"],
        data["q"]["y_mean"],
        color=color_q,
        label="Q",
    )
    plt.fill_between(
        data["q"]["x"],
        data["q"]["y_mean"] - data["q"]["y_std"],
        data["q"]["y_mean"] + data["q"]["y_std"],
        color=color_q,
        alpha=0.2,
    )
    # Plot the SG2 data
    plt.plot(
        data["sg2"]["x"],
        data["sg2"]["y_mean"],
        color=color_sg2,
        label="SG2",
    )
    plt.fill_between(
        data["sg2"]["x"],
        data["sg2"]["y_mean"] - data["sg2"]["y_std"],
        data["sg2"]["y_mean"] + data["sg2"]["y_std"],
        color=color_sg2,
        alpha=0.2,
    )
    # Plot the G1 data
    plt.plot(
        data["g1"]["x"],
        data["g1"]["y_mean"],
        color=color_g1,
        label="G1",
    )
    plt.fill_between(
        data["g1"]["x"],
        data["g1"]["y_mean"] - data["g1"]["y_std"],
        data["g1"]["y_mean"] + data["g1"]["y_std"],
        color=color_g1,
        alpha=0.2,
    )
    # Plot the D data
    plt.plot(   
        data["d"]["x"],
        data["d"]["y_mean"],
        color=color_d,
        label="D",
    )
    plt.fill_between(
        data["d"]["x"],
        data["d"]["y_mean"] - data["d"]["y_std"],
        data["d"]["y_mean"] + data["d"]["y_std"],
        color = color_d,
        alpha=0.2,
    )

    # Plot the H data
    plt.plot(
        data["h"]["x"],
        data["h"]["y_mean"],
        color=color_h,
        label="H",
    )

    plt.fill_between(
        data["h"]["x"],
        data["h"]["y_mean"] - data["h"]["y_std"],
        data["h"]["y_mean"] + data["h"]["y_std"],
        color=color_h,
        alpha=0.2,
    )
    
    # Plot the total data
    plt.plot(
        data["total"]["x"],
        data["total"]["y_mean"],
        color=color_total,
        label="Total",
        linestyle="dashed",
    )

    plt.fill_between(
        data["total"]["x"],
        data["total"]["y_mean"] - data["total"]["y_std"],
        data["total"]["y_mean"] + data["total"]["y_std"],
        color=color_total,
        alpha=0.2,
    )

    # Plot the living data
    plt.plot(
        data["living"]["x"],
        data["living"]["y_mean"],
        color=color_living,
        label="Living",
        linestyle="dashed",
    )

    plt.fill_between(
        data["living"]["x"],
        data["living"]["y_mean"] - data["living"]["y_std"],
        data["living"]["y_mean"] + data["living"]["y_std"],
        color=color_living,
        alpha=0.2,
    )

    plt.xlim((60,160))
    # plt.ylim((0, 8000))
    plt.xlabel("Time (Days)")
    plt.ylabel("Tumor Cell Count")
    plt.legend()
    plt.tight_layout()
    # Save PDF and PNG
    plt.savefig(folder + "/tumor_cell_count.pdf") 
    plt.savefig(folder + "/tumor_cell_count.png")

    




if __name__ == "__main__":
    # Get the directory where this script is located
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Find all JSON files in the directory
    directory = os.path.join(
        dir_path, "../../angiogenesis/output"
    )
    directory = os.path.abspath(directory)
    json_files, treatment_plan = GetAllJSONFiles(directory)
    print(json_files)

    # Load the data
    data = []
    for filename in json_files:
        with open(filename, "r") as f:
            data.append(json.load(f))
    with open(treatment_plan, "r") as f:
        treatment_plan = json.load(f)


    # Process the data
    data = [SimplifyDictionary(d) for d in data]
    data = [ComputeAdditionalTimeSeries(d) for d in data]

    # Aggregate the data
    data = AggregateData(data)

    # Plot the aggregated data
    PlotAggregatedData(data, treatment_plan, directory)
