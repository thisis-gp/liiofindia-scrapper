import re
import os

def clean_legal_text(text: str) -> str:
    """Specialized cleaner for Indian legal documents"""
    # Remove headers
    text = re.sub(r'2024 INSC \d+', '', text)

    # Remove page numbers/headers
    text = re.sub(r'Page \d+ of \d+', '', text)
    # Keep the first occurrence of the CIVIL APPEAL header
    match = re.search(r'CIVIL APPEAL NO. \d+ OF \d+', text)
    if match:
        appeal_header = match.group(0)
        text = re.sub(r'CIVIL APPEAL NO. \d+ OF \d+', '', text)  # Remove all occurrences
        text = text.replace("VERSUS", f"{appeal_header}\n\nVERSUS", 1)  # Reinsert the first one
    
    # Remove empty brackets from OCR artifacts
    text = re.sub(r'\(\s*\)', '', text)
    
    # Remove timestamps/digital signatures
    text = re.sub(r'Digitally signed by.*?Reason:\s*\n', '', text, flags=re.DOTALL)

    # Normalize whitespace, but preserve paragraph breaks
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Preserve paragraph breaks
    text = re.sub(r'[ \t]+', ' ', text) # normalize horizontal whitespace
    text = re.sub(r'\n{3,}', '\n\n', text) # remove extra newlines
    text = text.strip()

    # Remove "Signature Not Verified"
    text = re.sub(r'Signature Not Verified', '', text)
    
   # Remove citations like "1 AIR 1961 SC 1747" or "2 2022 SCC OnLine SC 1026"
    text = re.sub(r'\d+\s*(AIR|SCC OnLine)\s*\d+\s*[A-Z]+\s*\d+', '', text)
    
    return text


def clean_text_files_in_folder(input_folder: str, output_folder: str):
    """Cleans text files in the input folder and saves them to the output folder."""

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()

            cleaned_text = clean_legal_text(text)

            output_path = os.path.join(output_folder, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)


input_folder = 'supreme_court_texts'
output_folder = 'supreme_court_cleaned_texts' 
clean_text_files_in_folder(input_folder, output_folder)