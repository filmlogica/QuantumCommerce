import stripe
from scraper import get_best_sellers, DROPSHIPPING_SITES

# Set up Stripe API key
STRIPE_API_KEY = "your-stripe-secret-key"
stripe.api_key = STRIPE_API_KEY

def filter_high_demand_products():
    """Filters best-selling products from top dropshipping sites."""
    selected_products = []
    
    for site, url in DROPSHIPPING_SITES.items():
        best_sellers = get_best_sellers(url)
        for product in best_sellers[:5]:  # Select top 5 from each site
            if "premium" in product.lower() or "smart" in product.lower():  # Simple filtering for high-value items
                selected_products.append(product)

    return selected_products

def upload_to_stripe(product_name):
    """Uploads selected products to Stripe."""
    try:
        product = stripe.Product.create(
            name=product_name,
            description=f"{product_name} - AI-selected bestseller",
            type="good",
            active=True
        )

        price = stripe.Price.create(
            product=product.id,
            unit_amount=14999,  # $149.99 (adjust dynamically later)
            currency="usd",
            recurring={"interval": "month"}  # Subscription model
        )

        print(f"Uploaded to Stripe: {product.name} at ${price.unit_amount / 100}")
        return product.id
    except Exception as e:
        print(f"Error uploading to Stripe: {e}")
        return None

if __name__ == "__main__":
    print("🔎 Selecting High-Demand Dropshipping Products...")
    
    top_products = filter_high_demand_products()
    
    print("\n🚀 Uploading Selected Products to Stripe:")
    for product in top_products:
        stripe_id = upload_to_stripe(product)
        if stripe_id:
            print(f"✅ {product} successfully listed on Stripe!")
