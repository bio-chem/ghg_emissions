import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data_path = "ghg_with_income_and_continent.csv"  # Ensure the CSV file is in the same directory
df = pd.read_csv(data_path)

# List of EU27 countries (2023 membership)
eu27_countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands",
    "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"
]

# Filter data
df_eu27 = df[df['Country'].isin(eu27_countries)]
df_continents = df.groupby("Continent").sum(numeric_only=True).reset_index()

# Add total GHG emissions by year
df_eu27['Total GHG Emissions'] = df_eu27.iloc[:, 2:].sum(axis=1)
df_continents['Total GHG Emissions'] = df_continents.iloc[:, 1:].sum(axis=1)
total_world_emissions = df.iloc[:, 2:].sum(axis=0).sum()

# Streamlit app
st.title("GHG Emissions Contribution - EU27 and Continents")

# Country contribution
st.header("Contribution of Individual EU27 Countries to Total World GHG Emissions")
selected_year = st.slider("Select Year", min_value=1970, max_value=2023, value=2023)
year_col = str(selected_year)

df_eu27_year = df_eu27[["Country", year_col]].copy()
df_eu27_year["Contribution to Total GHG (%)"] = (df_eu27_year[year_col] / total_world_emissions) * 100

# Plot EU27 country contributions
fig_eu27 = px.bar(
    df_eu27_year,
    x="Country",
    y="Contribution to Total GHG (%)",
    title=f"EU27 Countries' GHG Emission Contribution in {selected_year}",
    labels={"Country": "EU27 Countries", "Contribution to Total GHG (%)": "Contribution (%)"},
    template="plotly_white",
    color="Country",
)

# Update layout for better presentation
fig_eu27.update_layout(
    title=dict(x=0.5, font=dict(size=18)),
    xaxis_title="EU27 Countries",
    yaxis_title="Contribution to Total GHG (%)",
    xaxis_tickangle=-45,
    margin=dict(l=40, r=40, t=40, b=120),
)

# Display the plot
st.plotly_chart(fig_eu27)

# Continent contribution
st.header("Contribution of Continents to Total World GHG Emissions")
df_continents_year = df_continents[["Continent", year_col]].copy()
df_continents_year["Contribution to Total GHG (%)"] = (df_continents_year[year_col] / total_world_emissions) * 100

# Plot continent contributions
fig_continent = px.pie(
    df_continents_year,
    values="Contribution to Total GHG (%)",
    names="Continent",
    title=f"Continents' GHG Emission Contribution in {selected_year}",
    template="plotly_white",
)
st.plotly_chart(fig_continent)

# Footer 
st.markdown(
    "Data source: `ghg_with_income_and_continent.csv` | EU27 Membership and Continent breakdown based on 2023 data."
)
