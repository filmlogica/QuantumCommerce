import requests
from bs4 import BeautifulSoup

# Define websites to scrape
DROPSHIPPING_SITES = {
    "Amazon": "https://www.amazon.com/Best-Sellers/zgbs",
    "AliExpress": "https://bestselling.aliexpress.com",
    "CJ Dropshipping": "https://www.cjdropshipping.com/category/bestseller/",
    "Spocket": "https://www.spocket.co/bestsellers",
    "SaleHoo": "https://www.salehoo.com/labs/trending-products",
    "Zendrop": "https://www.zendrop.com/trending-products"
}

def get_best_sellers(url):
    """Scrapes best-selling product listings from a given URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        products = []

        # Scrape Amazon bestsellers
        if "amazon" in url:
            for item in soup.select(".p13n-sc-truncate"):
                products.append(item.get_text(strip=True))

        # Scrape AliExpress bestsellers
        elif "aliexpress" in url:
            for item in soup.select(".item-title"):
                products.append(item.get_text(strip=True))

        # Scrape CJ Dropshipping bestsellers
        elif "cjdropshipping" in url:
            for item in soup.select(".product-title"):
                products.append(item.get_text(strip=True))

        # Scrape Spocket bestsellers
        elif "spocket" in url:
            for item in soup.select(".product-card-title"):
                products.append(item.get_text(strip=True))

        return products
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

if __name__ == "__main__":
    print("Scraping Best-Selling Products...")

    for site, url in DROPSHIPPING_SITES.items():
        best_sellers = get_best_sellers(url)
        print(f"\n🔥 {site} Best Sellers:")
        for product in best_sellers[:5]:  # Show top 5 products per site
            print(f"- {product}")

