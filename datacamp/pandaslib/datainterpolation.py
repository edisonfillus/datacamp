import pandas as pd
import numpy as np

ts1 = pd.DataFrame([
    ['2016-07-01', 0],
    ['2016-07-02', 1],
    ['2016-07-03', 2],
    ['2016-07-04', 3],
    ['2016-07-05', 4],
    ['2016-07-06', 5],
    ['2016-07-07', 6],
    ['2016-07-08', 7],
    ['2016-07-09', 8],
    ['2016-07-10', 9],
    ['2016-07-11', 10],
    ['2016-07-12', 11],
    ['2016-07-13', 12],
    ['2016-07-14', 13],
    ['2016-07-15', 14],
    ['2016-07-16', 15],
    ['2016-07-17', 16]],  columns=['Date', 'Value'])

ts1.index = pd.to_datetime(ts1['Date'])
del ts1['Date']


ts2 = pd.DataFrame([
    ['2016-07-01', 0],
    ['2016-07-04', 1],
    ['2016-07-05', 2],
    ['2016-07-06', 3],
    ['2016-07-07', 4],
    ['2016-07-08', 5],
    ['2016-07-11', 6],
    ['2016-07-12', 7],
    ['2016-07-13', 8],
    ['2016-07-14', 9],
    ['2016-07-15', 10]], columns=['Date', 'Value'])

ts2.index = pd.to_datetime(ts2['Date'])
del ts2['Date']

print(ts2)

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

print(ts2_interp)

# Compute the absolute difference of ts1 and ts2_interp: differences
differences = np.abs(ts1 - ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())