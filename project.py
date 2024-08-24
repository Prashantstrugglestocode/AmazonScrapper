from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os

try:
    # Set up Firefox options
    options = Options()
    options.headless = True  # Run in headless mode

    driver = webdriver.Firefox(options=options)
    query = input("The thing you want to search for\n")
    file = 0
    n = int(input("Enter the number of pages you want to be scanned: \n"))
    country_code = input("Enter the country code you want\n")

    # Ensure the output directory exists
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, n+1):
        driver.get(f"https://www.amazon.{country_code}/s?k={query}&page={i}")
        time.sleep(4)  # Wait for the page to load

        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        print(f"{len(elems)} items found on page {i}")
        
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"{output_dir}/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1

    driver.close()
except Exception as e:
    print(f"Error: {e}")
