# This file contains helper functions to methods performed in the respective Jupyter Notebooks files
# contained within the same folder.

# Imports
import seaborn as sns  # for visualization
import matplotlib.pyplot as plt  # for visualization


# Plot Scatter-Plot
def plot_scatter(data, x, y):
    """
    :param:
        data: A Pandas DataFrame
        x: A list, NumPy Series, or 1D Array list structure for the x-axis
        y: A list, NumPy Series, or 1D Array list structure for the x-axis

    :return:
        Scatter plot of x and y values
    """

    scatter = sns.scatterplot(data=data, x=x, y=y)
    plt.show()
    return scatter


# Visualize Clusters
def plot_clusters(data, x, y, c):
    """
    :param
        data: A Pandas DataFrame
        x: A list, NumPy Series, or 1D Array list structure for the x-axis
        y: A list, NumPy Series, or 1D Array list structure for the x-axis
        c: A list, NumPy Series, or 1D Array list structure to color the points within the scatter plot

    :return:
        Scatter plot of x vs y colored by c
    """

    scatter = sns.scatterplot(data=data, x=x, y=y, hue=c)
    plt.show()
    return scatter
