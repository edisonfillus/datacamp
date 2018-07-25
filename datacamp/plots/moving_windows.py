# Import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd

stocks = pd.read_csv('./data/stocks.csv', parse_dates=True, index_col='Date')
aapl = stocks['AAPL']
ibm = stocks['IBM']
csco = stocks['CSCO']
msft = stocks['MSFT']

# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2, 2, 1)
plt.plot(aapl.rolling('30d').mean(), color='green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2, 2, 2)
plt.plot(aapl.rolling('75d').mean(), color='red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(aapl.rolling('125d').mean(), color='magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2, 2, 4)
plt.plot(aapl.rolling('250d').mean(), color='cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

# Display the plot
plt.show()


# Plot std_30 in red
plt.plot(aapl.rolling('30d').std(), color='red', label='30d')

# Plot std_75 in cyan
plt.plot(aapl.rolling('75d').std(), color='cyan', label='75d')

# Plot std_125 in green
plt.plot(aapl.rolling('125d').std(),color='green', label='125d')

# Plot std_250 in magenta
plt.plot(aapl.rolling('250d').std(),color='magenta', label='250d')

# Add a legend to the upper left
plt.legend(loc='upper left')

# Add a title
plt.title('Moving standard deviations')

# Display the plot
plt.show()
