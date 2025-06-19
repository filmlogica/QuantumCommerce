import json
import logging
from backend.data.fetch_data import fetch_market_data

logging.basicConfig(level=logging.INFO)

def create_prompt():
    """Generate AI prompts using the latest financial data."""
    data = fetch_market_data()
    
    prompts = {
        "basic": f"Analyze the latest financial trends using stock market data: {data['yfinance']}, financial metrics: {data['finnhub']}, and consumer interest trends: {data['pytrends']}. Summarize key shifts for {data['industry']} sector.",
        
        "pro": f"Generate a detailed market analysis for {data['industry']} integrating stock trends: {data['yfinance']}, financial indicators: {data['finnhub']}, and Pytrends consumer demand insights: {data['pytrends']}. Recommend competitive strategies.",
        
        "enterprise": f"Construct an advanced business intelligence report based on: Stock trends ({data['yfinance']}), financial performance ({data['finnhub']}), and consumer search behavior ({data['pytrends']}). Forecast sector growth for {data['industry']}."
    }

    with open("backend/prompts/latest_prompt.json", "w") as file:
        json.dump(prompts, file, indent=4)

    logging.info("AI prompts generated and saved successfully!")

if __name__ == "__main__":
    create_prompt()
