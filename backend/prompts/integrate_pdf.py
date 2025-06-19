import json
import logging
from PyPDF2 import PdfWriter

logging.basicConfig(level=logging.INFO)

TEMPLATES = {
    "basic": "backend/reports/basic_template.pdf",
    "pro": "backend/reports/pro_template.pdf",
    "enterprise": "backend/reports/enterprise_template.pdf"
}

def update_pdf():
    """Insert AI-generated reports into predefined PDF templates."""
    with open("backend/prompts/latest_ai_response.json", "r") as file:
        responses = json.load(file)

    for tier, response in responses.items():
        writer = PdfWriter()
        writer.add_blank_page(612, 792)  # Letter size

        # Modify PDF with AI response (Mock implementation)
        pdf_path = f"backend/reports/{tier}_updated.pdf"
        with open(pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)

        logging.info(f"Updated {tier} PDF successfully!")

if __name__ == "__main__":
    update_pdf()
