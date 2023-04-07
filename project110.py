import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

data = pd.read_csv('medium_data.csv')

datan = data['reading_time'].to_list()

population_mean = statistics.mean(datan)

def display(list):
    mean = statistics.mean(list)
    graph = ff.create_distplot([datan],['Medium Data'],show_hist = False)
    graph.add_trace(go.Scatter(x=[mean,mean], y=[0,0], mode='lines', name='Mean'))
    graph.show()

def randomData(count):
    dataset = []
    for i in range(count):
        integer = random.randint(0,len(datan))
        value = datan[integer]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def randomData30times():
    _30dtat100times = []
    for i in range(100):
        count = randomData(30)
        _30dtat100times.append(count)
    display(_30dtat100times)
    mean = statistics.mean(_30dtat100times)
    print("Mean of sample data 100 times is {}".format(mean))

randomData30times()
print("population mean is {}".format(population_mean))
