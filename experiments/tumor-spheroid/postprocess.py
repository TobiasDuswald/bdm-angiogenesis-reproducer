import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def GetAllJSONFiles(folder):
    """ Finds all JSON files in any subdirectory of folder. Returns list."""
    import os

    data_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("json") and "time-series-data" in file:
                data_files.append(os.path.join(root, file))
    return data_files


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

def PlotData(data, folder):
    color_q = "#EDC728"
    color_sg2 = "#1A9C13"
    color_g1 = "#69ED15"
    color_d = "#000000"
    color_h = "#A0A0A0"
    color_living = "#A51313"
    color_proliferating = "#e377c2"
    color_total = "#307EC9"

    # Set the figure size
    plt.figure(figsize=(4, 3))

    # Plot the Q data
    plt.plot(
        data["q"]["x"],
        data["q"]["y"],
        color=color_q,
        label="Q",
    )
    # Plot the SG2 data
    plt.plot(
        data["sg2"]["x"],
        data["sg2"]["y"],
        color=color_sg2,
        label="SG2",
    )
    # Plot the G1 data
    plt.plot(
        data["g1"]["x"],
        data["g1"]["y"],
        color=color_g1,
        label="G1",
    )
    # Plot the D data
    plt.plot(   
        data["d"]["x"],
        data["d"]["y"],
        color=color_d,
        label="D",
    )
    # Plot the H data
    plt.plot(
        data["h"]["x"],
        data["h"]["y"],
        color=color_h,
        label="H",
    )

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
        dir_path, "results"
    )
    directory = os.path.abspath(directory)
    json_files = GetAllJSONFiles(directory)
    print(json_files)

    # Load the data
    data = []
    for filename in json_files:
        with open(filename, "r") as f:
            data.append(json.load(f))

    # Process the data
    data = [SimplifyDictionary(d) for d in data]
    data = [ComputeAdditionalTimeSeries(d) for d in data]

    # Iterate over data with enumerate
    for i, d in enumerate(data):
        json_file = json_files[i]
        directory = os.path.dirname(json_file)
        PlotData(d, directory)
