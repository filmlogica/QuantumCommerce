from PyPDF2 import PdfWriter
import os

def create_pdf(content, filename):
    """Generate a PDF report."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)  # Standard letter size
    
    file_path = f"./reports/{filename}"
    with open(file_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"PDF {filename} created successfully!")
    return file_path

# Example Usage
pdf_path = create_pdf("Sample AI-generated report", "sample_report.pdf")
