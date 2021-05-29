import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random

data=pd.read_csv('medium_data.csv')
read_time=data['reading_time']

population_mean=statistics.mean(read_time)
print("Population Mean=\t",population_mean)

def sampleMean():
    dataset=[]
    for i in range(0,30):
        index1=random.randint(0,len(read_time)-1)
        value=read_time[index1]
        dataset.append(value)
    sampleMean=statistics.mean(dataset)
    return sampleMean

def setup():
    mean_list_samples=[]

    for i in range(0,100):
        list_of_mean=sampleMean()
        mean_list_samples.append(list_of_mean)

    meanList=statistics.mean(mean_list_samples)
    stdev_meanList=statistics.stdev(mean_list_samples)
    print("Mean List={},Stdev Mean List={}".format(meanList,stdev_meanList))

    figure=ff.create_distplot([mean_list_samples],["Sample Mean"],show_hist=False)
    figure.show()

setup()




