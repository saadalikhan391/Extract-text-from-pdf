import sys
from pdfminer.high_level import extract_text

# Function to extract text from a PDF file
def extract_pdf_text(pdf_path):
    text = extract_text(pdf_path)
    return text

# Check if the correct number of command-line arguments is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <path_to_pdf>")
    sys.exit(1)

# Get the PDF file path from the command-line arguments
pdf_path = sys.argv[1]

# Extract text content from the PDF file
text_content = extract_pdf_text(pdf_path)

# Write the extracted text to an output file named 'output.txt'
with open('output_pdf.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)

# Print a success message
print("Text extracted successfully! Check output.txt for your content.")