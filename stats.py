# -*- coding: utf-8 -*-
"""
Created on Mon Aug 5 13:46:52 2024

@author: W. R. T. Fanka
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

#You may need to install Orca. In your Anaconda terminal, use:
#conda install -c plotly plotly-orca

# Data: Replace with own data
data = [0.0269, 0.04, 0.055, 0.055, 0.076, 0.085, 0.087, 0.087, 0.099, 0.099, 0.099, 0.065, 0.067, 0.07, 0.072, 0.088, 0.09, 0.09, 0.099, 
        0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 
        0.099, 0.099, 0.099, 0.099, 0.099, 0.099, 0.1, 0.102, 0.104, 0.099, 0.099, 0.105, 0.105, 0.108, 0.108, 0.109, 0.109, 0.109, 0.116, 
        0.119, 0.12, 0.123, 0.124, 0.134, 0.134, 0.137, 0.139, 0.146, 0.148, 0.149, 0.149, 0.15, 0.15, 0.15, 0.154, 0.155, 0.157, 0.16, 
        0.165, 0.165, 0.167, 0.167, 0.1677, 0.169, 0.171, 0.172, 0.174, 0.178, 0.178, 0.179, 0.179, 0.181, 0.188, 0.189, 0.189, 0.192, 
        0.195, 0.197, 0.201, 0.207, 0.21, 0.21, 0.239, 0.24, 0.242, 0.243, 0.245, 0.245, 0.247, 0.254, 0.257, 0.26, 0.262, 0.271, 0.28, 
        0.28, 0.287, 0.288, 0.299, 0.3, 0.307, 0.31, 0.214, 0.215, 0.216, 0.226, 0.229, 0.246, 0.246, 0.265, 0.265, 0.268, 0.294, 0.297, 
        0.298, 0.311, 0.314, 0.319, 0.321, 0.34, 0.344, 0.348, 0.349, 0.352, 0.353, 0.357, 0.363, 0.363, 0.366, 0.383, 0.39, 0.396, 0.399, 
        0.408, 0.408, 0.409, 0.409, 0.41, 0.416, 0.421, 0.426, 0.429, 0.429, 0.43, 0.436, 0.437, 0.439, 0.441, 0.441, 0.443, 0.454, 0.468, 
        0.481, 0.487, 0.534, 0.534, 0.546, 0.548, 0.593, 0.601, 0.624, 0.628, 0.491, 0.498, 0.503, 0.506, 0.522, 0.548, 0.549, 0.555, 
        0.592, 0.638, 0.66, 0.672, 0.682, 0.687, 0.69, 0.691, 0.786, 0.795, 0.804, 0.953, 0.983, 0.989, 0.82, 1.012, 0.694, 0.704, 0.712, 
        0.72, 0.728, 0.835, 0.877, 0.909, 0.952, 1.026, 1.032, 1.062, 1.16]

# Create DataFrame
df = pd.DataFrame(data, columns=["Values"])
data = df["Values"]
#%%

# Create a DataFrame
df = pd.DataFrame({'Values': data})

# Calculate Frequency
df['Frequency'] = df['Values'].map(df['Values'].value_counts())

# Calculate Relative Frequency
df['Relative Frequency'] = df['Frequency'] / len(df)

# Calculate Cumulative Frequency
df['Cumulative Frequency'] = df['Frequency'].cumsum()

# Calculate Cumulative Relative Frequency
df['Cumulative Relative Frequency'] = df['Cumulative Frequency'] / len(df)

# Save to an Excel file
df.to_excel('statistics.xlsx', index=False)  # Specify the file name

# Display the DataFrame
print(df)
#%%

freq = {}
for value in data:
    freq[value] = freq.get(value, 0) + 1

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sorted_values = sorted(data)
plt.plot(sorted_values, [freq[value] for value in sorted_values], 
         marker='.')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Frequency Polygon")

plt.tight_layout()
plt.show()
#%%

# Check for properties of symmetry
# Apply logarithmic transformation
transformed_data = np.log1p(data)  # Adding 1 to avoid log(0)

# Plot histograms before and after transformation
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, edgecolor='black')
plt.title("Original Data")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(transformed_data, bins=30, edgecolor='black')
plt.title("Log-Transformed Data")
plt.xlabel("Log(Values)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
#%%

# Calculate Skewness
skewness = skew(df["Values"])
print("Skewness:", skewness)
#%%

# S/R greater than 0.9
count = (df['Values'] > .9).sum()
print('Values greater than 0.9: ', count)

# Percentage
count_values = df['Values'].value_counts().sum()
perc = count/count_values*100
print('Percentage of values greater than 0.9: ', perc, '%')
#%%

# S/R less than 0.7
count = (df['Values'] < .7).sum()
print('Values less than 0.7: ', count)

# Percentage
perc = count/count_values*100
print('Percentage of values less than 0.7: ', perc, '%')
#%%

# Define the range
min_value = 0.3
max_value = 0.6999

# Count values within the range
count = df['Values'].between(min_value, max_value).sum()

print(f"Number of values between {min_value} and {max_value}: {count}")

# Percentage
perc = count/count_values*100
print(f"Percentage of values between {min_value} and {max_value}: {perc}", '%')
#%%
