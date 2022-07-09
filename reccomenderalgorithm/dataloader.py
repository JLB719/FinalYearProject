import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent;


def loadInData():
    """
    Reads in data from the csv file and converts it to a 2d array.
    Also converts '.'s to ',' in the genres field
    Returns

    """
    dataload = []
    with open(str(BASE_DIR) + '/reccomenderalgorithm/data.csv', 'r') as file:
        reader = csv.reader(file)
        firstline = True
        for row in reader:
            if not firstline:
                dataload.append(row)
            else:
                firstline = False
    converteddata = []
    for row in dataload:
        newadd = []
        count = 0
        for datapoint in row:
            if count == 9:

                toadd = datapoint.split(".")
                newadd.append(toadd)
            else:
                newadd.append(datapoint)
            count += 1
        converteddata.append(newadd)
    return converteddata
