import sys, numpy as np
from utils.read_csv import read_csv_by_column
from scipy.stats.stats import spearmanr

if len(sys.argv) != 3:
    sys.exit("usage: python spearman.py [num_variables] ***.csv: the number of variables should be the same as the number of columns in the csv file")
    
columns = []
var = int(sys.argv[1])
for i in range (1, (var+1)):
    columns.append("column " + str(i))
#print columns

values = read_csv_by_column(sys.argv[2], columns)
ylength = len(values[columns[0]])
inp = np.ndarray(shape=(var, ylength))

for i in range(0, len(columns)):
    inp[i] = values[columns[i]]

(rho, pval) = spearmanr(inp, axis=1)

print rho
print pval