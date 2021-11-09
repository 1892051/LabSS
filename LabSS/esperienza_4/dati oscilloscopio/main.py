import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100

def dataExtractor(rawData):
    return {
        'unit': rawData[0],
        'data': rawData[1:]
        }

def parseCsv(path):
    df = pd.read_csv(path)

    columns = df.columns
    x_axis = dataExtractor(df[columns[0]])

    #iterate through the other columns
    y_axis = []
    for column in columns[1:]:
        y_axis.append(dataExtractor(df[column]))
    return {
        'x': x_axis,
        'y': y_axis
        }

def plot(plotData):
    fig,ax = plt.subplots(1)
    ax.plot(plotData['x']['data'], plotData['y'][0]['data'],'-')
    ax.set_ylabel(plotData['y'][0]['unit'])
    ax.set_xlabel(plotData['x']['unit'])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.show()

plot(parseCsv(r'scope_10.csv'))
print(type([]) == list)