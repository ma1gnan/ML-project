import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load and prepare data
df = pd.read_csv(
    "data/merged_energy_weather_2years.csv",
    parse_dates=["period"],
)
df = df.sort_values("period") # Sort by date

# Plot: hourly electricity demand over time
fig, ax = plt.subplots(figsize=(9, 4), dpi=200)
ax.plot(df["period"], df["demand_mw"], linewidth=0.5, color="#1f4e8c")

ax.set_xlabel("Date")                               # Set x-axis label
ax.set_ylabel("Electricity Demand (MW)")            # Set y-axis label
ax.set_title("Hourly Electricity Demand — SOCO Balancing Authority (May 2024 – Apr 2026)") # Set title

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()                                  # Auto-format the x-axis labels for better readability


ax.grid(alpha=0.3)                                   # Add grid lines
plt.tight_layout()                                   # Adjust layout to prevent clipping of labels
plt.savefig("demand_over_time.png", dpi=200)         # Save the figure as a PNG file
plt.close()

print("Saved demand_over_time.png")
