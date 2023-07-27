from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import csv
import time
import os
import winsound

# Setup Selenium
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.set_page_load_timeout(30)  # Set a 30-second timeout for loading pages

websites = []

# Open the CSV file
with open('../websites300to355.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Website"])  # Write the header

    for page_number in range(300, 5000):  # Loop through pages 1 to 5
        while True:  # Keep trying to load the page until it succeeds
            try:
                print(f"Loading page {page_number}...")
                url = f"https://myip.ms/browse/sites/{page_number}/ownerID/376714/ownerIDii/"
                driver.get(url)

                print("Finding rows...")
                # Find the table and rows
                table = driver.find_element(By.ID, 'sites_tbl')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                break  # If the table and rows are found, break out of the loop
            except (NoSuchElementException, TimeoutException):
                # If the table is not found or the page load times out, assume a captcha is present
                print("Captcha detected or page load timed out. Please solve it if necessary and then press Enter to continue.")
                winsound.Beep(1000, 500)  # Play a beep sound
                input()

        for row in rows:
            # Find all columns in the row
            cols = row.find_elements(By.TAG_NAME, 'td')

            # Make sure there are at least two columns
            if len(cols) > 1:
                # Get the text from the second column
                website = cols[1].text
                websites.append(website)

                # Write the website to the CSV file
                writer.writerow([website])

        # Wait for a while before loading the next page
        time.sleep(5)

print("Done.")
driver.quit()
