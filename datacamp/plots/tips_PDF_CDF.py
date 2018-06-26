# Probability density functions (PDFs) and Cumulative density functions (CDFs).
# PDF, you need to specify normed=True in your call to .hist()
# CDF, you need to specify cumulative=True in addition to normed=True

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/tips.csv')

df['fraction'] = df['tip'] / df['total_bill']

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0,.3))

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', normed=True, bins=30, cumulative=True, range=(0,.3))
plt.show()
