import sys, numpy as np
from utils.read_csv import read_csv_by_column
from scipy.stats import ttest_1samp, ttest_ind

if len(sys.argv) != 3:
    sys.exit("usage: python [paired/unpaired] t_test.py ***.csv")

"""
Let's say we only compare two data values at a time right now.
"""
columns = ["col1", "col2"]
values = read_csv_by_column("data/pre_post.csv", columns)

if sys.argv[1] == "paired":
    x = values[columns[0]]
    y = values[columns[1]]
    x = x-y
    # paired t-test: doing two measurments on the same experimental unit
    # e.g., before and after a treatment
    t_statistic, p_value = ttest_1samp(x, 0.0)

    # p < 0.05 => alternative hypothesis:
    # the difference in mean is not equal to 0
    print "paired t-test", p_value
    