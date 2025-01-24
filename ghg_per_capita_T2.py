import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged dataset
ghg_df = pd.read_csv("ghg_with_income.csv")

# Filter necessary columns (2023 GHG emissions and Income Category)
ghg_df = ghg_df[["Income Category", "2023"]].dropna()

# Group by income category and sum GHG emissions for 2023
aggregated_ghg = ghg_df.groupby("Income Category")["2023"].sum().reset_index()

# Sort
income_order = ["Low-income countries", "Lower-middle-income countries", "Upper-middle-income countries", "High-income countries"]
aggregated_ghg["Income Category"] = pd.Categorical(aggregated_ghg["Income Category"], categories=income_order, ordered=True)
aggregated_ghg = aggregated_ghg.sort_values("Income Category")

# Shortened labels for better readability
short_labels = {
    "Low-income countries": "Low",
    "Lower-middle-income countries": "Lower-Mid",
    "Upper-middle-income countries": "Upper-Mid",
    "High-income countries": "High"
}
aggregated_ghg["Short Label"] = aggregated_ghg["Income Category"].map(short_labels)
sns.set_style("whitegrid")

# Create the bar plot
plt.figure(figsize=(8, 5))
palette = sns.color_palette("pastel")
sns.barplot(
    data=aggregated_ghg,
    x="Short Label",
    y="2023",
    palette=palette
)

# Add labels and title
plt.xlabel("Income Groups", fontsize=12)
plt.ylabel("GHG Emissions per Capita (2023)", fontsize=12)
plt.title("GHG Emissions by Income Group (2023)", fontsize=14, weight="bold")



# Save the plot
plt.tight_layout()
plt.savefig("ghg_emissions_by_income_group.png")


plt.show()
