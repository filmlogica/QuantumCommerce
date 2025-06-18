from flask import Blueprint, request, jsonify
from backend.config.celery_config import generate_report
from backend.database.models import Report, db
import datetime

report_bp = Blueprint('report_generation', __name__)

# Generate Report (Instant Request via Celery)
@report_bp.route('/generate', methods=['POST'])
def generate_report_request():
    data = request.get_json()
    industry = data.get("industry")
    tier = data.get("tier")

    if not industry or not tier:
        return jsonify(error="Industry and tier required"), 400

    # Trigger Celery async task
    task = generate_report.delay(industry, tier)

    return jsonify(task_id=task.id, message="Report generation started")

# Fetch Latest Report (From Database)
@report_bp.route('/latest', methods=['GET'])
def get_latest_report():
    industry = request.args.get("industry")
    tier = request.args.get("tier")

    if not industry or not tier:
        return jsonify(error="Industry and tier required"), 400

    report = Report.query.filter_by(industry=industry, tier=tier).order_by(Report.generated_at.desc()).first()

    if not report:
        return jsonify(error="No report available"), 404

    return jsonify(
        industry=report.industry,
        tier=report.tier,
        content=report.content,
        generated_at=report.generated_at.strftime("%Y-%m-%d %H:%M:%S")
    )

# Scheduled Report Generation (Runs in Background)
@report_bp.route('/scheduled', methods=['POST'])
def scheduled_report_generation():
    industries = ["Retail", "Tech", "Finance"]
    tiers = ["Basic", "Pro", "Enterprise"]

    for industry in industries:
        for tier in tiers:
            generate_report.delay(industry, tier)

    return jsonify(message="Scheduled report generation started")
