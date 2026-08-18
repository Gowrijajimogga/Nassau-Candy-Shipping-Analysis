import pandas as pd

# Load dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Dataset shape
print("DATASET SHAPE:")
print(df.shape)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Data types
print("\nDATA TYPES:")
print(df.dtypes)

# Basic statistics
print("\nBASIC STATISTICS:")
print(df.describe())

# Total sales
print("\nTOTAL SALES:")
print(df["Sales"].sum())

# Total units sold
print("\nTOTAL UNITS SOLD:")
print(df["Units"].sum())

# Total gross profit
print("\nTOTAL GROSS PROFIT:")
print(df["Gross Profit"].sum())

# Total cost
print("\nTOTAL COST:")
print(df["Cost"].sum())





# TOP 10 PRODUCTS BY SALES

print("\nTOP 10 PRODUCTS BY SALES:")

top_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_sales)


# TOP 10 PRODUCTS BY GROSS PROFIT

print("\nTOP 10 PRODUCTS BY GROSS PROFIT:")

top_profit = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_profit)

# SALES BY REGION
print("\nSALES BY REGION:")

sales_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_region)


# GROSS PROFIT BY REGION
print("\nGROSS PROFIT BY REGION:")

profit_region = (
    df.groupby("Region")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_region)


# SALES BY SHIP MODE
print("\nSALES BY SHIP MODE:")

sales_ship = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_ship)


# UNITS SOLD BY SHIP MODE
print("\nUNITS SOLD BY SHIP MODE:")

units_ship = (
    df.groupby("Ship Mode")["Units"]
    .sum()
    .sort_values(ascending=False)
)

print(units_ship)


# MONTHLY SALES TREND
print("\nMONTHLY SALES TREND:")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print(monthly_sales)



# TOP 10 PRODUCTS BY UNITS SOLD
print("\nTOP 10 PRODUCTS BY UNITS SOLD:")

top_units = (
    df.groupby("Product Name")["Units"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_units)


# BOTTOM 10 PRODUCTS BY SALES
print("\nBOTTOM 10 PRODUCTS BY SALES:")

bottom_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print(bottom_sales)


# ==============================
# DATA VISUALIZATION
# ==============================

import matplotlib.pyplot as plt


# 1. SALES BY REGION
plt.figure(figsize=(8, 5))

sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
#plt.show()


# 2. SALES BY SHIP MODE
plt.figure(figsize=(8, 5))

sales_ship.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()


# 3. MONTHLY SALES TREND
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
#plt.show()


# TOP 10 CUSTOMERS BY SALES

print("\nTOP 10 CUSTOMERS BY SALES:")

top_customers = (
    df.groupby("Customer ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)


# TOP 10 CUSTOMERS BY GROSS PROFIT

print("\nTOP 10 CUSTOMERS BY GROSS PROFIT:")

top_customer_profit = (
    df.groupby("Customer ID")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customer_profit)


# SALES BY DIVISION

print("\nSALES BY DIVISION:")

sales_division = (
    df.groupby("Division")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_division)


# GROSS PROFIT BY DIVISION

print("\nGROSS PROFIT BY DIVISION:")

profit_division = (
    df.groupby("Division")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_division)

# PROFIT MARGIN BY DIVISION

print("\nPROFIT MARGIN BY DIVISION:")

division_summary = df.groupby("Division").agg({
    "Sales": "sum",
    "Gross Profit": "sum"
})

division_summary["Profit Margin %"] = (
    division_summary["Gross Profit"] /
    division_summary["Sales"] * 100
)

print(division_summary.sort_values(
    "Profit Margin %",
    ascending=False
))

# ==============================
# DATA VISUALIZATION
# ==============================

import matplotlib.pyplot as plt

# 1. SALES BY REGION
plt.figure(figsize=(8, 5))
sales_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. GROSS PROFIT BY REGION
plt.figure(figsize=(8, 5))
profit_region.plot(kind="bar")
plt.title("Gross Profit by Region")
plt.xlabel("Region")
plt.ylabel("Gross Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. SALES BY SHIP MODE
plt.figure(figsize=(8, 5))
sales_ship.plot(kind="bar")
plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. UNITS SOLD BY SHIP MODE
plt.figure(figsize=(8, 5))
units_ship.plot(kind="bar")
plt.title("Units Sold by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. MONTHLY SALES TREND
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. TOP 10 CUSTOMERS BY SALES

plt.figure(figsize=(10, 5))
top_customers.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()


# 7. TOP 10 CUSTOMERS BY GROSS PROFIT

plt.figure(figsize=(10, 5))
top_customer_profit.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Gross Profit")
plt.xlabel("Gross Profit")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()


# 8. TOP 10 PRODUCTS BY SALES

plt.figure(figsize=(10, 6))
top_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()


# 9. SALES BY DIVISION

plt.figure(figsize=(8, 5))
sales_division.plot(kind="bar")

plt.title("Sales by Division")
plt.xlabel("Division")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 10. GROSS PROFIT BY DIVISION

plt.figure(figsize=(8, 5))
profit_division.plot(kind="bar")

plt.title("Gross Profit by Division")
plt.xlabel("Division")
plt.ylabel("Gross Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 11. PROFIT MARGIN BY DIVISION

plt.figure(figsize=(8, 5))
division_summary["Profit Margin %"].sort_values().plot(kind="bar")

plt.title("Profit Margin by Division")
plt.xlabel("Division")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==========================================
# SAVE ANALYSIS RESULTS
# ==========================================

# Save Top 10 Customers by Sales
top_customers.to_csv("top_10_customers_sales.csv")

# Save Top 10 Customers by Gross Profit
top_customer_profit.to_csv("top_10_customers_profit.csv")

# Save Top 10 Products by Sales
top_sales.to_csv("top_10_products_sales.csv")

# Save Sales by Division
sales_division.to_csv("sales_by_division.csv")

# Save Gross Profit by Division
profit_division.to_csv("profit_by_division.csv")

# Save Profit Margin by Division
division_summary.to_csv("division_profit_margin.csv")

print("\nAll analysis results have been saved successfully!")

# ==========================================
# FINAL BUSINESS INSIGHTS
# ==========================================

print("\n" + "=" * 50)
print("FINAL BUSINESS INSIGHTS")
print("=" * 50)

# Best region
best_region = sales_region.idxmax()
print(f"\n1. Best performing region: {best_region}")
print(f"   Sales: {sales_region.max():.2f}")

# Best ship mode
best_ship_mode = sales_ship.idxmax()
print(f"\n2. Most used ship mode: {best_ship_mode}")
print(f"   Sales: {sales_ship.max():.2f}")

# Best division
best_division = sales_division.idxmax()
print(f"\n3. Best performing division: {best_division}")
print(f"   Sales: {sales_division.max():.2f}")

# Most profitable division
best_profit_division = profit_division.idxmax()
print(f"\n4. Most profitable division: {best_profit_division}")
print(f"   Gross Profit: {profit_division.max():.2f}")

# Highest profit margin
best_margin_division = division_summary["Profit Margin %"].idxmax()
best_margin = division_summary["Profit Margin %"].max()

print(f"\n5. Highest profit margin: {best_margin_division}")
print(f"   Profit Margin: {best_margin:.2f}%")

print("\n" + "=" * 50)
print("PROJECT ANALYSIS COMPLETED")
print("=" * 50)

# ==========================================
# FINAL SALES DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Sales by Region
sales_region.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Sales by Region")
axes[0, 0].set_xlabel("Region")
axes[0, 0].set_ylabel("Sales")
axes[0, 0].tick_params(axis="x", rotation=0)

# 2. Sales by Ship Mode
sales_ship.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Sales by Ship Mode")
axes[0, 1].set_xlabel("Ship Mode")
axes[0, 1].set_ylabel("Sales")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Sales by Division
sales_division.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Sales by Division")
axes[1, 0].set_xlabel("Division")
axes[1, 0].set_ylabel("Sales")
axes[1, 0].tick_params(axis="x", rotation=0)

# 4. Gross Profit by Division
profit_division.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Gross Profit by Division")
axes[1, 1].set_xlabel("Division")
axes[1, 1].set_ylabel("Gross Profit")
axes[1, 1].tick_params(axis="x", rotation=0)

plt.suptitle("NASSAU SHIPPING - SALES & PROFIT DASHBOARD",
             fontsize=16)

plt.tight_layout()
plt.show()