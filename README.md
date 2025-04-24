# Supreme Court Case Scraper, PDF to Text Converter, and Text Cleaner

This repository contains three Python scripts designed to automate the process of:

1.  **Scraping** case links from the LII of India website for the year 2024.
2.  **Downloading** the PDF files associated with these case links.
3.  **Extracting** text content from the downloaded PDF files.
4.  **Cleaning** the extracted text specifically for Indian Supreme Court judgments.

## Scripts Included

* **`scrapper.py`**: This script uses Selenium to navigate the LII of India website, extracts links to individual Supreme Court cases from 2024, and downloads the corresponding PDF files.
* **`pdf_2_text.py`**: This script processes all PDF files within a specified directory, extracts the text content from each PDF using the `fitz` library (PyMuPDF), and saves the extracted text into individual `.txt` files in a designated output directory.
* **`clean_text.py`**: This script takes the extracted text files as input and applies a series of regular expressions to clean the text, removing common artifacts found in Indian legal documents such as headers, page numbers, digital signatures, and citations.

## Setup and Usage

### Prerequisites

* **Python 3.x** installed on your system.
* **Chrome Browser** installed (as Selenium uses ChromeDriver).

### Installation

1.  **Clone the repository** (if you have it as a repository).
2.  **Navigate to the project directory** in your terminal.
3.  **Install the required dependencies** using pip:

    ```bash
    pip install -r requirements.txt
    ```


### Configuration

You can customize the behavior of the scripts by modifying the following variables within each file:

#### `scrapper.py`

* **`base_url`**: This variable (currently set to `"http://www.liiofindia.org/in/cases/cen/INSC/2024/"`) defines the starting URL for scraping case links. **You can change this URL** if you want to scrape cases from a different year or section of the website.
* **Download Directory**: The PDFs will be downloaded to a directory named `supreme_court_pdfs` in the same directory where you run the script. You can change the name of this directory within the `download_pdf` function if needed:

    ```python
    os.makedirs('your_custom_pdf_directory', exist_ok=True)
    filename = os.path.join('your_custom_pdf_directory', pdf_url.split('/')[-1])
    ```

#### `pdf_2_text.py`

* **`pdf_directory`**: This variable (currently set to `"/home/gurupriyan/Desktop/Internship Assignment/Lexiscope/Backend/supreme_court_pdfs"`) specifies the directory where the PDF files to be processed are located. **You need to change this path** to the actual location of your downloaded PDF files.
* **`output_directory`**: This variable (currently set to `"/home/gurupriyan/Desktop/Internship Assignment/Lexiscope/Backend/supreme_court_texts"`) defines the directory where the extracted text files will be saved. **You need to change this path** to your desired output location.

#### `clean_text.py`

* **`input_folder`**: This variable (currently set to `'supreme_court_texts'`) specifies the directory containing the text files to be cleaned. **Ensure this matches the `output_directory` you set in `pdf_2_text.py`**.
* **`output_folder`**: This variable (currently set to `'supreme_court_cleaned_texts'`) defines the directory where the cleaned text files will be saved. **You can change this path** to your desired output location for the cleaned text.

### Running the Scripts

1.  **Scrape and Download PDFs:**
    Navigate to the project directory in your terminal and run:
    ```bash
    python scrapper.py
    ```
    This will create a `supreme_court_pdfs` directory (or your custom directory) and download the PDF files.

2.  **Convert PDFs to Text:**
    Ensure the `pdf_directory` variable in `pdf_2_text.py` points to the directory containing the downloaded PDFs. Then, run:
    ```bash
    python pdf_2_text.py
    ```
    This will create a `supreme_court_texts` directory (or your custom directory) and save the extracted text files.

3.  **Clean the Text Files:**
    Ensure the `input_folder` variable in `clean_text.py` points to the directory containing the extracted text files (from the previous step) and the `output_folder` variable is set to your desired location for the cleaned files. Then, run:
    ```bash
    python clean_text.py
    ```
    This will create a `supreme_court_cleaned_texts` directory (or your custom directory) and save the cleaned text files.

After running these scripts, you will have a directory containing cleaned text versions of the Supreme Court case judgments downloaded from the specified LII of India URL. You can then use these cleaned text files for further analysis or processing.
