import numpy as np 
import csv

def getDataSource(dataPath):
    marks = []
    days = []
    with open (dataPath) as f:
        ds= csv.DictReader(f)
        for i in ds:
            marks.append(float(i["Marks In Percentage"]))
            days.append(float(i["Days Present"]))

    return{"x":marks, "y":days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Marks in percentage and Days present :- \n--->",correlation[0,1])

def setup():
    dataPath="dataset1.csv"
    dataSource= getDataSource(dataPath)
    findCorrelation(dataSource)
setup()
