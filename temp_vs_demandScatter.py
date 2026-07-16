"""

Generates a scatter plot of temperature versus hourly electricity demand
for the SOCO balancing authority (May 2024 - April 2026).

"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load and prepare data 
df = pd.read_csv(
    "data/merged_energy_weather_2years.csv",
    parse_dates=["period"],
)
df = df.sort_values("period")

# Plot: temperature vs. electricity demand
fig, ax = plt.subplots(figsize=(6, 5), dpi=200)
ax.scatter(
    df["temperature_f"],
    df["demand_mw"],
    s=2,
    alpha=0.15,
    color="#c1440e",
)

ax.set_xlabel("Temperature (°F)")
ax.set_ylabel("Electricity Demand (MW)")
ax.set_title("Temperature vs. Electricity Demand")

ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("temp_vs_demand.png", dpi=200)
plt.close()

print("Saved temp_vs_demand.png")
