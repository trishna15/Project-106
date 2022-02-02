import numpy as np
import csv

def getDataSource(dataPath):
    coffee=[]
    hours=[]
    with open (dataPath) as f:
        ds= csv.DictReader(f)
        for i in ds:
            coffee.append(float(i["Coffee in ml"]))
            hours.append(float(i["sleep in hours"]))

    return{"x":coffee , "y":hours}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Cups of Coffee and Hours of Sleep :- \n--->",correlation[0,1])

def setup():
    dataPath="dataset2.csv"
    dataSource= getDataSource(dataPath)
    findCorrelation(dataSource)
setup()



