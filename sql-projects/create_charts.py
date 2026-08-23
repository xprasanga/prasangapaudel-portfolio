import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

repo = Path(__file__).resolve().parents[2]

results = repo / "sql-projects" / "results"
output = repo / "docs" / "sql-projects" / "figures"

output.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# 1. Revenue by Product
# ---------------------------------------------------------

product = pd.read_csv(results / "product_revenue.csv")

product = product.sort_values("revenue")

plt.figure(figsize=(9, 5))
plt.barh(product["product_name"], product["revenue"])

plt.xlabel("Revenue ($)")
plt.ylabel("")
plt.title("Revenue by Product")

plt.tight_layout()
plt.savefig(output / "product-revenue.png", dpi=180)
plt.close()

# ---------------------------------------------------------
# 2. Revenue by Category
# ---------------------------------------------------------

category = pd.read_csv(results / "category_sales.csv")

category = category.sort_values("revenue")

plt.figure(figsize=(8, 5))
plt.barh(category["category"], category["revenue"])

plt.xlabel("Revenue ($)")
plt.ylabel("")
plt.title("Revenue by Product Category")

plt.tight_layout()
plt.savefig(output / "category-revenue.png", dpi=180)
plt.close()


# ---------------------------------------------------------
# 3. Monthly Revenue
# ---------------------------------------------------------

monthly = pd.read_csv(results / "monthly_sales.csv")

plt.figure(figsize=(9, 5))
plt.plot(
    monthly["month"],
    monthly["revenue"],
    marker="o",
    linewidth=2
)

plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.title("Monthly Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(output / "monthly-revenue.png", dpi=180)
plt.close()


print("Charts created successfully:")
print(output / "product-revenue.png")
print(output / "category-revenue.png")
print(output / "monthly-revenue.png")