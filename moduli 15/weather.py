import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD CSV
# =========================

df = pd.read_csv("weather_data.csv")

# Show column names
print(df.columns)

# =========================
# TEMPERATURE COLUMN
# =========================

# Use second column as temperature
temperature_column = df.columns[1]

# Clean temperature values
df[temperature_column] = df[temperature_column].astype(str)

# Extract only numbers
df[temperature_column] = df[temperature_column].str.extract(r'(\d+\.?\d*)')[0]

# Convert to numeric
df[temperature_column] = pd.to_numeric(
    df[temperature_column],
    errors="coerce"
)

# Remove empty values
df = df.dropna()

# =========================
# 1. TEMPERATURE OVERVIEW
# =========================

average_temperature = df[temperature_column].mean()

print("\nAverage Temperature:")
print(f"{average_temperature:.2f} °C")

# =========================
# 2. MONTHLY TEMPERATURE
# =========================

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_data = []

size = len(df) // 12

for i in range(12):

    start = i * size
    end = (i + 1) * size

    month_avg = df[temperature_column][start:end].mean()

    monthly_data.append(month_avg)

# Print monthly averages
print("\nMonthly Average Temperatures:\n")

for month, temp in zip(months, monthly_data):
    print(f"{month}: {temp:.2f} °C")

# Bar plot
plt.figure(figsize=(12,6))

plt.bar(months, monthly_data)

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)

plt.show()

# =========================
# 3. HIGHS AND LOWS
# =========================

highest_temp = df[temperature_column].max()
lowest_temp = df[temperature_column].min()

print("\n========================")
print("HIGHS AND LOWS")
print("========================")

print(f"Hottest Temperature: {highest_temp} °C")
print(f"Coldest Temperature: {lowest_temp} °C")

print("\nHottest Day Data:")
print(df[df[temperature_column] == highest_temp])

print("\nColdest Day Data:")
print(df[df[temperature_column] == lowest_temp])

# =========================
# 4. TEMPERATURE TRENDS
# =========================

print("\n========================")
print("TEMPERATURE TRENDS")
print("========================")

# Create line graph
plt.figure(figsize=(14,6))

plt.plot(df[temperature_column])

plt.title("Temperature Changes Over Time")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.show()