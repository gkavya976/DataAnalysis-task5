import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first rows
print("Dataset:")
print(df.head())

# Basic information
print("\nDataset Info:")
print(df.info())

# Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)
category_sales.plot(
    kind="bar",
    title="Sales by Category"
)

plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(
    df["Date"].dt.month
)["Sales"].sum()

monthly_sales.plot(
    kind="line",
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()