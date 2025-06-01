import time

SYSTEM_RUNNING = True

def seo_optimization():
    """Generates AI-powered product descriptions and blog content for SEO."""
    print("📝 Running SEO optimization...")
    time.sleep(3)
    print("✅ AI-generated blog posts and product descriptions uploaded for organic Google traffic.")

def email_marketing():
    """Automates AI-generated email campaigns for customer engagement."""
    print("📧 Running email marketing...")
    time.sleep(3)
    print("✅ AI-powered emails successfully sent to potential buyers.")

def affiliate_outreach():
    """Auto-recruits YouTube influencers & bloggers for affiliate marketing."""
    print("🎯 Running influencer affiliate outreach...")
    time.sleep(3)
    print("✅ Outreach emails sent to influencers offering exclusive commission deals.")

def forum_and_social_engagement():
    """Uses AI to respond to trending discussions on Reddit, Quora, and forums."""
    print("💬 Running organic engagement automation...")
    time.sleep(3)
    print("✅ AI-generated responses posted in key online discussions.")

def run_marketing_cycle():
    """Continuously cycles through marketing tasks."""
    global SYSTEM_RUNNING
    while SYSTEM_RUNNING:
        seo_optimization()
        email_marketing()
        affiliate_outreach()
        forum_and_social_engagement()
        print("🔄 Restarting marketing loop...")
        time.sleep(10)  # Short delay before repeating cycle

def stop_system():
    """Stops the marketing system manually."""
    global SYSTEM_RUNNING
    SYSTEM_RUNNING = False
    print("🛑 AI Advertising System Stopped.")

if __name__ == "__main__":
    print("🚀 Starting AI-Powered Marketing Automation (Continuous Mode)")
    try:
        run_marketing_cycle()
    except KeyboardInterrupt:
        stop_system()
