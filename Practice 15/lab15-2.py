import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# Reading data from the CSV file and parsing 'Date' as datetime
file_path = 'comptagevelo2014.csv'
df = pd.read_csv(file_path, sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True)

# Set 'Date' as the index
df.set_index('Date', inplace=True)
df.index = pd.to_datetime(df.index)  # Convert the index to DatetimeIndex

# Display the first few rows of the DataFrame
print(df.head(3))

# Check the available column names
print(df.columns)

# Choose a column name from the available columns
chosen_column = 'Rachel / Papineau'  # Replace with the column name you want to plot

# Create a plot for the chosen column
plt.plot(df.index, df[chosen_column], label=chosen_column)

# Resample the data (assuming the 'Date' column is a datetime type)
monthly_sum = df.resample('M').sum()

# Applying your code to display the plot
most_popular_month = monthly_sum.sum(axis=1).idxmax().strftime('%B %Y')

plt.title(f'Most Popular Month: {most_popular_month}')
plt.xlabel('Date')
plt.ylabel('Number of Cyclists')
plt.legend()
plt.show()
