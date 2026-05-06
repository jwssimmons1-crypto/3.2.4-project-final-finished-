'''''''''''
import pandas as pd
import matplotlib.pyplot as plt

# Load the honey production data
df = pd.read_csv("operations.csv")

# Remove commas from Value column and convert to numeric
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Drop rows with NaN (formerly "(D)" values)
df = df.dropna(subset=['Value'])

# Get a list of unique states and years
unique_states = df['State'].unique()
unique_years = df['Year'].unique()

# Initialize lists to store results
all_honey = []
all_states = []

# Loop through each state, group by year, and sum honey production
for state in unique_states:
    honey_data = df[df['State'] == state].groupby('Year')['Value']
    honey_sums = honey_data.sum()
    all_honey.append(honey_sums)
    all_states.append(state)

# Print each state and its total honey production for validation
for i in range(len(all_states)):
    print(all_states[i], all_honey[i].sum())

# --- Graph 1: Large Producers (total > 10,000,000 lbs) ---
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if honey.sum() > 1_000:
        years = honey.keys()
        plt.plot(years, honey, marker='o', linestyle='-', linewidth=2, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Top Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 2: Mid-Level Producers (total between 1,000,000 and 10,000,000 lbs) ---
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if 200 <= honey.sum() <= 1_000:
        years = honey.keys()
        plt.plot(years, honey, marker='s', linestyle='--', linewidth=1.5, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Production (lbs)")
plt.title("Mid-Level Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 3: Small Producers (total < 1,000,000 lbs) ---
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if honey.sum() < 200:
        years = honey.keys()
        plt.plot(years, honey, marker='^', linestyle=':', linewidth=1, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Small Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 4: Average honey production per year for all states (no legend) ---
plt.figure()
for state in unique_states:
    honey_means = df[df['State'] == state].groupby('Year')['Value'].mean()
    years = honey_means.keys()
    plt.plot(years, honey_means, marker='D', linestyle='-.', linewidth=1)
plt.xlabel("Year")
plt.ylabel("Average Operations per County")
plt.title("Average Operations per State Over Time")
plt.show()

# --- Graph 5: Total honey production per year (bar chart) ---
yearly_totals = []
yearly_keys = []

for year in unique_years:
    totals = df[df['Year'] == year].groupby('Year')['Value']
    totals_sum = totals.sum()
    yearly_totals.append(totals_sum.sum())
    yearly_keys.append(year)

# Print yearly totals for validation
print("\nYearly Totals:")
for i in range(len(yearly_keys)):
    print(yearly_keys[i], yearly_totals[i])

# Plot yearly totals as a bar chart with edge color for style
plt.figure()
plt.bar(yearly_keys, yearly_totals, color='steelblue', edgecolor='navy', width=1.5)
plt.xlabel("Year")
plt.ylabel("Total Number of Operations")
plt.title("Total U.S. Honey Operations by Year")
plt.show()
'''''''''''''''

import pandas as pd
import matplotlib.pyplot as plt

# Load the operations data
df = pd.read_csv("operations.csv")

# Convert to numeric (handles "(L)" and "(D)" values)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Drop rows with NaN (formerly "(D)" values)
df = df.dropna(subset=['Value'])

# Get a list of unique states and years
unique_states = df['State'].unique()
unique_years = df['Year'].unique()

# Initialize lists to store results
all_honey = []
all_states = []

# Loop through each state, group by year, and sum operations
for state in unique_states:
    honey_data = df[df['State'] == state].groupby('Year')['Value']
    honey_sums = honey_data.sum()
    all_honey.append(honey_sums)
    all_states.append(state)

# Print each state and its total operations for validation
for i in range(len(all_states)):
    print(all_states[i], all_honey[i].sum())

# Graph 1: Large States (total > 2,500 operations) 
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if honey.sum() > 2_500:
        years = honey.keys()
        plt.plot(years, honey, marker='o', linestyle='-', linewidth=2, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Top Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# Graph 2: Mid-Level States (total between 500 and 2,500 operations) 
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if 500 <= honey.sum() <= 2_500:
        years = honey.keys()
        plt.plot(years, honey, marker='s', linestyle='--', linewidth=1.5, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Mid-Level Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# Graph 3: Small States (total < 500 operations) 
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if honey.sum() < 500:
        years = honey.keys()
        plt.plot(years, honey, marker='^', linestyle=':', linewidth=1, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Small Honey Producing States by Number of Operations")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# Graph 4: Average operations per year for all states (no legend)
plt.figure()
for state in unique_states:
    honey_means = df[df['State'] == state].groupby('Year')['Value'].mean()
    years = honey_means.keys()
    plt.plot(years, honey_means, marker='D', linestyle='-.', linewidth=1)
plt.xlabel("Year")
plt.ylabel("Average Operations per County")
plt.title("Average Operations per State Over Time")
plt.show()

# Graph 5: Total operations per year (bar chart) 
yearly_totals = []
yearly_keys = []

for year in unique_years:
    totals = df[df['Year'] == year].groupby('Year')['Value']
    totals_sum = totals.sum()
    yearly_totals.append(totals_sum.sum())
    yearly_keys.append(year)

# Print yearly totals for validation
print("\nYearly Totals:")
for i in range(len(yearly_keys)):
    print(yearly_keys[i], yearly_totals[i])

# Plot yearly totals as a bar chart with edge color for style
plt.figure()
plt.bar(yearly_keys, yearly_totals, color='steelblue', edgecolor='navy', width=1.5)
plt.xlabel("Year")
plt.ylabel("Total Number of Operations")
plt.title("Total U.S. Honey Operations by Year")
plt.show()

# Graph 6: All states operations over time 
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    years = honey.keys()
    plt.plot(years, honey, marker='o', linestyle='-', linewidth=2, label=state)
plt.xlabel("Year")
plt.ylabel("Number of Operations")
plt.title("Honey Operations by State Over Time")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()