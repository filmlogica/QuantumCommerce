from celery import Celery

# Celery Configuration
celery = Celery(
    'quantumcommerce',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Celery settings
celery.conf.update(
    task_routes={
        'tasks.generate_report': {'queue': 'reports'},
        'tasks.update_market_data': {'queue': 'updates'}
    },
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True
)

# Scheduled Tasks (Hourly Report Updates)
@celery.task
def update_market_data():
    from backend.tasks import fetch_google_trends, fetch_yahoo_finance
    trends = fetch_google_trends()
    finance_data = fetch_yahoo_finance()
    return {"google_trends": trends, "finance_data": finance_data}

@celery.task
def generate_report(industry, tier):
    data = update_market_data()
    report = f"Industry: {industry}, Tier: {tier}\n"
    report += f"Google Trends: {data['google_trends']}\n"
    report += f"Finance Insights: {data['finance_data']}\n"
    return report
