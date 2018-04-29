import pandas as pd
import matplotlib.pyplot as plt

# Read the file into a DataFrame: df
df = pd.read_csv('./data/dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the info of df
print(df.info())

# Print the describe for 'Proposed Height' (Work only for numeric data)
print(df['Proposed Height'].describe())

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

# Create the boxplot
df.boxplot(column='Proposed Height', by='Borough', rot=90)

# Display the plot
plt.show()


# Create and display the first scatter plot
df.plot(kind='scatter', x='Proposed Height', y='Existing Height', rot=70)
plt.show()