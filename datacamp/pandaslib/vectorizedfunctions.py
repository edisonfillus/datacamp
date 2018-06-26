# Import zscore from scipy.stats
from scipy.stats import zscore
import pandas as pd

election = pd.read_csv('./data/pennsylvania2012_turnout.csv')

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore =zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())
