import pandas as pd
import matplotlib.pyplot as plt

# Sample business sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [25000, 30000, 28000, 35000, 40000, 45000],
    "Profit": [5000, 7000, 6000, 9000, 11000, 13000],
    "Orders": [100, 120, 110, 140, 160, 180]
}

df = pd.DataFrame(data)

# Calculate KPIs
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Orders"].sum()
avg_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("===== BUSINESS KPI DASHBOARD =====")
print(f"Total Revenue: Rs. {total_revenue:,}")
print(f"Total Profit: Rs. {total_profit:,}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: Rs. {avg_order_value:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

print("\nMonthly Business Data:")
print(df)

# Create dashboard charts
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(df["Month"], df["Revenue"], marker="o")
axes[0].set_title("Monthly Revenue")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Revenue (Rs.)")
axes[0].grid(True)

axes[1].bar(df["Month"], df["Profit"])
axes[1].set_title("Monthly Profit")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Profit (Rs.)")

plt.tight_layout()
plt.savefig("business_kpi_dashboard.png")
plt.show()

print("\nDashboard generated successfully!")
