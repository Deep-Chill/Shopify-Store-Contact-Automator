from tkinter import Tk, Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import csv
import itertools
import time
import os
import winsound
import re

### websites1.csv completed to row 374
### websites300to355 completed to row 167

# Setup Selenium
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.set_page_load_timeout(30)  # Set a 30-second timeout for loading pages
driver.maximize_window()

# Create the Tkinter window
root = Tk()
root.attributes('-topmost', 1)  # Keep the window always on top
button = Button(root, text="Continue to next website", font=('Helvetica', '20'), height=5, width=20, bg='blue', fg='white')
button.pack()

def continue_to_next_website():
    # This function will be called when the button is clicked
    root.quit()

# Open the CSV file with the websites
with open('../websites300to355.csv', 'r') as file:
    reader = csv.reader(file)
    rows_to_skip = 1
    for _ in itertools.islice(reader, rows_to_skip):
        pass
    # next(reader)  # Skip the header

    # Open the CSV file to save the email addresses
    with open('../emails.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Website", "Email"])  # Write the header

        for row in reader:
            website = row[0]
            # Add "http://" to the beginning of the URL if it's not already there
            if not website.startswith('http://') and not website.startswith('https://'):
                website = 'http://' + website
            print(f"Loading website {website}...")
            driver.get(website)

            try:
                # Try to find a link with the text "Contact" or "Contact Us"
                contact_link = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Contact')))
                print("Contact page found. Opening...")
                contact_link.click()
                # time.sleep(2)  # Wait for the contact page to load
                # Fill in the contact form
                try:
                    name_field = driver.find_element(By.NAME, 'name')
                    name_field.send_keys('Noman Bukhari')
                except NoSuchElementException:
                    print("Name field not found.")
                try:
                    email_field = driver.find_element(By.NAME, 'email')
                    email_field.send_keys('Noman@ebox3pl.com')
                except NoSuchElementException:
                    print("Email field not found.")
                try:
                    phone_field = driver.find_element(By.NAME, 'phone')
                    phone_field.send_keys('3502049113')
                except NoSuchElementException:
                    print("Phone field not found.")
                winsound.Beep(1000, 500)  # Play a beep sound
                button.config(command=continue_to_next_website)
                root.mainloop()
            except NoSuchElementException:
                print("Contact page not found. Looking for email address...")
                # Try to find an email address on the page
                body_text = driver.find_element(By.TAG_NAME, 'body').text
                match = re.search(r'[\w\.-]+@[\w\.-]+', body_text)
                if match:
                    email = match.group(0)
                    print(f"Email address found: {email}")
                    writer.writerow([website, email])
                else:
                    print("Email address not found.")
            except ElementClickInterceptedException:
                print("Element click was intercepted by another element. Trying to continue...")
                winsound.Beep(1000, 500)  # Play a beep sound
                button.config(command=continue_to_next_website)
                root.mainloop()
            except TimeoutException:
                print("Contact link was not clickable after waiting. Trying to continue...")
                winsound.Beep(1000, 500)  # Play a beep sound
                button.config(command=continue_to_next_website)
                root.mainloop()
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                winsound.Beep(1000, 500)  # Play a beep sound
                button.config(command=continue_to_next_website)
                root.mainloop()

print("Done.")
driver.quit()
