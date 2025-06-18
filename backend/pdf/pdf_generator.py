from PyPDF2 import PdfWriter

writer = PdfWriter()
writer.add_blank_page(width=612, height=792)  # Standard letter size

with open("sample.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("PDF created successfully!")
