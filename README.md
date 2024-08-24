

# Amazon Web Scraper

This project is designed to scrape product information from Amazon pages and save the data into a CSV file. It consists of two main scripts: `project.py` for scraping data and `collection.py` for processing and saving the data.

## Features

- **Headless Browsing**: Uses headless mode to run the browser in the background.
- **Data Extraction**: Extracts product titles, prices, and links.
- **Data Saving**: Saves the extracted data into a CSV file, sorted by price.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Firefox WebDriver (geckodriver)
- Required Python packages: `selenium`, `beautifulsoup4`, `pandas`

You can install the required Python packages using pip:

```bash
pip install selenium beautifulsoup4 pandas
```

## Setup WebDriver

1. Download and install `geckodriver` from [Mozilla's GitHub releases](https://github.com/mozilla/geckodriver/releases).
2. Ensure `geckodriver` is accessible from your PATH.

## Running the Scripts

### 1. Run `project.py`

The `project.py` script is responsible for scraping the data from Amazon and saving it as HTML files.

- **Inputs**:
  - **Search Query**: The product you want to search for (e.g., "laptops").
  - **Number of Pages**: The number of pages to scrape.
  - **Country Code**: The country code for the Amazon domain (e.g., "com", "de", "uk").

- **Command**:
  ```bash
  python project.py
  ```

- This will create HTML files in the `data` directory.

### 2. Run `collection.py`

The `collection.py` script processes the saved HTML files, extracts the relevant data, and saves it into a CSV file.

- **Command**:
  ```bash
  python collection.py
  ```

- **What It Does**:
  - Reads HTML files from the `data` directory.
  - Extracts product titles, prices, and links.
  - Sorts the data by price in ascending order.
  - Saves the results to `output.csv`.

## Example

1. Execute `project.py` to scrape data:
   ```bash
   python project.py
   ```

2. Then run `collection.py` to process and save the data:
   ```bash
   python collection.py
   ```

3. Check the `output.csv` file for the sorted data.

## Error Handling

If errors occur during the execution of either script, an error message will be printed.

## Notes

- Ensure that the `data` directory exists and is properly populated by `project.py` before running `collection.py`.
- Modify the scripts as needed for different class names or data structures if the HTML structure of the Amazon page changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Adjust the instructions if there are any specific details or additional configurations for your project.
