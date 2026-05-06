import pandas as pd
import matplotlib.pyplot as plt

# Load the honey production data
df = pd.read_csv("honey.csv")

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
    if honey.sum() > 10_000_000:
        years = honey.keys()
        plt.plot(years, honey, marker='o', linestyle='-', linewidth=2, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Production (lbs)")
plt.title("Large Honey Producers by State")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 2: Mid-Level Producers (total between 1,000,000 and 10,000,000 lbs) ---
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if 1_000_000 <= honey.sum() <= 10_000_000:
        years = honey.keys()
        plt.plot(years, honey, marker='s', linestyle='--', linewidth=1.5, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Production (lbs)")
plt.title("Mid-Level Honey Producers by State")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 3: Small Producers (total < 1,000,000 lbs) ---
plt.figure()
for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    if honey.sum() < 1_000_000:
        years = honey.keys()
        plt.plot(years, honey, marker='^', linestyle=':', linewidth=1, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Production (lbs)")
plt.title("Small Honey Producers by State")
plt.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.show()

# --- Graph 4: Average honey production per year for all states (no legend) ---
plt.figure()
for state in unique_states:
    honey_means = df[df['State'] == state].groupby('Year')['Value'].mean()
    years = honey_means.keys()
    plt.plot(years, honey_means, marker='D', linestyle='-.', linewidth=1)
plt.xlabel("Year")
plt.ylabel("Average Honey Production (lbs)")
plt.title("Average Honey Production by State Over Time")
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
plt.ylabel("Total Honey Production (lbs)")
plt.title("Total U.S. Honey Production by Year")
plt.show()