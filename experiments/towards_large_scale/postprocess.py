import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

def ReadGrowthData(filename):
    growth_data = pd.read_csv(filename, sep=",", header=0)
    print(growth_data)
    return growth_data

def ConvertToVolume(n):
    factor = GetAgentToVolumeFactor()
    return n * factor

def ConvertToNumber(V):
    factor = GetVolumeToAgentFactor()
    return V * factor

def GetVolumeToAgentFactor():
    # Compute volume of a sphere with radius 9.953 microns
    r = 9.953 / 1000.0  # microns to mm
    V = 4.0 / 3.0 * np.pi * r**3
    return 0.64 / V

def GetAgentToVolumeFactor():
    # Compute volume of a sphere with radius 9.953 microns
    r = 9.953 / 1000.0  # microns to mm
    V = 4.0 / 3.0 * np.pi * r**3
    return V / 0.64

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
        new_data[data["data_"][i]["first"]]["x"] = (
            np.array(data["data_"][i]["second"]["x_values"]) * minutes_to_days
        )
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


def PlotSingleTimeSeries(data, growth_data):

    # Use LaTeX font
    plt.rc("text", usetex=True)

    # Subplots (two rows, one column) with shared x-axis
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(9, 6))

    # Cell count names
    cell_count_names_1 = [
        "q",
        "sg2",
        "g1",
        "d",
        "h",
    ]
    cell_count_names_2 = [
        "living",
        "proliferating",
        "total",
    ]
    colors = {
        "q": "#EDC728",
        "sg2": "#1A9C13",
        "g1": "#69ED15",
        "d": "#000000",
        "h": "#A0A0A0",
        "living": "darkorange",
        "proliferating": "seagreen",
        "total": "navy",
    }

    for key in cell_count_names_1:
        # print the last value
        print(key, data[key]["y"][-1])

    # Plot growth data, e.g. the column mean_1 against the column days. 
    # Then highlight the area given by the column std_1 around mean
    ax[1].plot(
        growth_data["days"] - 7,
        growth_data["mean_1"],
        color="lightsteelblue",
        marker="o",
        markersize=3,
        label="Growth data",
    )
    ax[1].fill_between(
        growth_data["days"] - 7,
        growth_data["mean_1"] - growth_data["std_1"],
        growth_data["mean_1"] + growth_data["std_1"],
        color="lightsteelblue",
        alpha=0.5,
    )

    for key in cell_count_names_1:
        label = key
        if len(label) < 4:
            label = label.upper()
        ax[0].plot(
            data[key]["x"],
            ConvertToVolume(data[key]["y"]),
            color=colors[key],
            label=label,
        )

    for key in cell_count_names_2:
        label = key
        if len(label) < 4:
            label = label.upper()
        ax[1].plot(
            data[key]["x"],
            ConvertToVolume(data[key]["y"]),
            color=colors[key],
            label=label,
        )


    # Set axis labels
    ax[0].set_ylabel("Tumor volume (mm$^3$)")
    ax[1].set_ylabel("Tumor volume (mm$^3$)")
    ax[1].set_xlabel("Time (days)")

    # Show legends
    ax[0].legend(loc="upper left")
    ax[1].legend(loc="upper left")

    # Add a second y-axis on both plots in order to show the cell count
    secax1 = ax[0].secondary_yaxis('right', functions=(ConvertToNumber, ConvertToVolume))
    secax1.set_ylabel('Number of cells')
    secax2 = ax[1].secondary_yaxis('right', functions=(ConvertToNumber, ConvertToVolume))
    secax2.set_ylabel('Number of cells')
    
    # # Show plot
    # plt.show()

    # Save plot
    filename = os.path.join(dir_path, "large-scale.pdf")
    filename = os.path.abspath(filename)
    fig.savefig(filename, bbox_inches="tight")

if __name__ == "__main__":
    # Get the directory where this script is located
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Read the input file
    filename = os.path.join(
        dir_path, "../../angiogenesis/output/angiogenesis/time-series-data.json"
    )
    filename = os.path.abspath(filename)
    with open(filename, "r") as f:
        data = json.load(f)

    # Read the growth data
    filename = os.path.join(
        dir_path, "../../angiogenesis/data/growth_data_combined.csv"
    )
    filename = os.path.abspath(filename)
    growth_data = ReadGrowthData(filename)

    # Process the data
    data = SimplifyDictionary(data)
    data = ComputeAdditionalTimeSeries(data)

    # Plot the data
    PlotSingleTimeSeries(data, growth_data)
