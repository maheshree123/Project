import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("volunteers.csv")

print("\n===== NayePankh Analytics Dashboard =====\n")

# Total Volunteers
total_volunteers = len(df)
print("Total Volunteers:", total_volunteers)

# Average Age
average_age = df["Age"].mean()
print("Average Age:", round(average_age, 2))

# Total Volunteer Hours
total_hours = df["Hours"].sum()
print("Total Volunteer Hours:", total_hours)

# City-wise Volunteer Count
city_count = df["City"].value_counts()

print("\nCity-wise Volunteers:")
print(city_count)

# Create Chart
plt.figure(figsize=(6,4))
city_count.plot(kind="bar")

plt.title("Volunteers by City")
plt.xlabel("City")
plt.ylabel("Number of Volunteers")

plt.tight_layout()

plt.savefig("charts.png")

plt.show()

print("\nChart saved as charts.png")