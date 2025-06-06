# Selects high-ticket, high-retention candidates from CSV or scraped JSON
import pandas as pd

def filter_high_ticket_products(filepath="data/products.csv"):
    df = pd.read_csv(filepath)
    filtered = df[(df["price"] > 500) & (df["recurring"] == True)]
    return filtered.sort_values("margin", ascending=False).head(10)

if __name__ == "__main__":
    top_products = filter_high_ticket_products()
    print("Top candidates:")
    print(top_products[["name", "price", "margin"]])
