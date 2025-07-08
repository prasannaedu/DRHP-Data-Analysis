import fitz
import pdfplumber
import json
import os

import json

# Load JSON file
json_file = "SAMBHV STEEL TUBES LIMITED_parsed.json"

try:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f" Error loading JSON file: {e}")
    exit(1)
except FileNotFoundError:
    print(f" File not found: {json_file}")
    exit(1)

# Debugging print statements
print(f" Type of data: {type(data)}")

if isinstance(data, list):
    print(f" Number of items in data: {len(data)}")

    if len(data) > 0:
        first_item = data[0]

        if isinstance(first_item, dict):
            print(f" Type of first element: {type(first_item)}")
            print(f" First element keys: {list(first_item.keys())}")
            print(f" First element sample:\n{json.dumps(first_item, indent=2)}")
        else:
            print(f" First element is not a dictionary. Found: {type(first_item)}")

else:
    print(" JSON structure is unexpected. Expected a list, but found:", type(data))
    exit(1)

#  Now continue with your existing logic in pdf_parser.py...
# Example: Process extracted sections, embed text, store results, etc.



def parse_pdf(pdf_path):
    try:
        document = fitz.open(pdf_path)
    except Exception as e:
        print(f" Error opening PDF: {e}")
        return None

    sections = []
    for page_num in range(len(document)):
        try:
            page = document.load_page(page_num)
            text = page.get_text("text")

            section = {
                "section_number": page_num + 1,
                "chapter_name": f"Chapter {page_num + 1}",
                "company_name": "Unknown",
                "full_text": text,
                "tables": [],
            }
            sections.append(section)

        except Exception as e:
            print(f" Error processing page {page_num + 1}: {e}")
            continue

    return sections

def process_multiple_pdfs(pdf_paths):
    for pdf_path in pdf_paths:
        filename = os.path.splitext(os.path.basename(pdf_path))[0]
        output_filename = f"{filename}_parsed.json"

        print(f" Processing PDF: {pdf_path}")
        parsed_data = parse_pdf(pdf_path)

        if parsed_data:
            with open(output_filename, "w", encoding="utf-8") as f:
                json.dump(parsed_data, f, indent=4)
            print(f" Parsed data saved to {output_filename}")
        else:
            print(f" Failed to parse {pdf_path}")

if __name__ == "__main__":
    pdf_paths = [
        "C:\\Users\\udumularahul\\OneDrive\\文件\SAMBHV STEEL TUBES LIMITED.pdf",
        "C:\\Users\\udumularahul\\OneDrive\\文件\\2nd.pdf",
        "C:\\Users\\udumularahul\\OneDrive\\文件\ADITYA INFOTECH LIMITED.pdf",
        "C:\\Users\\udumularahul\\OneDrive\文件\\Kumar Arch Tech Limited - DRHP.pdf"
    ]
    process_multiple_pdfs(pdf_paths)
