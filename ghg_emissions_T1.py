import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'ghg_totals.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print(data.head())

# Define the EDGAR codes for EU27 countries
eu27_codes = [
    'AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA',
    'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD',
    'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE'
]
# Filter for EU27 countries and calculate total emissions per year
eu27_data = data[data['EDGAR Country Code'].isin(eu27_codes)]
eu27_totals = eu27_data.iloc[:, 2:].sum()

# Calculate global total emissions per year
global_totals = data.iloc[:, 2:].sum()

# Combine data into a DataFrame for visualization
combined_data = pd.DataFrame({
    'Year': eu27_totals.index.astype(int),
    'EU27': eu27_totals.values,
    'Global': global_totals.values
})

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(combined_data['Year'], combined_data['EU27'], label='EU27', color='blue', marker='o')
plt.plot(combined_data['Year'], combined_data['Global'], label='Global', color='green', marker='o')
plt.title("Chart 1 - Evolution of GHG Growth in the Euro Area (EU27) and Worldwide", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("GHG Emissions (MtCO2e)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
