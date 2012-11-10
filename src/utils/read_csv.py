import csv, numpy as np

"""
Read csv file by column and put each entry into a column list

Parameters
----------
f: the file name in string
columns: list of names of the columns in the csv file.

Returns
-------
a dictionary type containing all the columns as lists.
"""
def read_csv_by_column(f, columns):
    res = dict()
    for column in columns:
        res[column] = np.array([])
    csvFile = csv.reader(open(f, "rb"))
    for row in csvFile:
        #print row
        for i in range(0, len(columns)):
            res[columns[i]] = np.append(res[columns[i]], float(row[i]))
    return res