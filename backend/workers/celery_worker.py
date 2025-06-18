from backend.config.celery_config import celery
from backend.database.models import Report, db
from backend.tasks import fetch_google_trends, fetch_yahoo_finance
from datetime import datetime

@celery.task
def scheduled_report_generation():
    industries = ["Retail", "Tech", "Finance"]
    tiers = ["Basic", "Pro", "Enterprise"]

    for industry in industries:
        for tier in tiers:
            generate_report.delay(industry, tier)

    return "Scheduled report generation triggered."

@celery.task
def generate_report(industry, tier):
    trends = fetch_google_trends(industry)
    finance_data = fetch_yahoo_finance(industry)

    report_content = f"Industry: {industry}, Tier: {tier}\n"
    report_content += f"Google Trends: {trends}\n"
    report_content += f"Finance Insights: {finance_data}\n"

    store_report(industry, tier, report_content)

    return f"Report generated for {industry} - {tier}"

def store_report(industry, tier, content):
    report = Report(
        industry=industry,
        tier=tier,
        content=content,
        generated_at=datetime.utcnow()
    )
    db.session.add(report)
    db.session.commit()
