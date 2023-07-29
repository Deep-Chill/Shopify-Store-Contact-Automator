**Shopify Store Information and Contact Form Automator**

This repository contains two Python scripts that automate the process of navigating to a list of Shopify stores, extracting their information, and finding and opening contact forms on their websites. I personally used it to contact many more stores per hour than I could have without it. It requires you to submit the forms manually, but it automatically loads the pages one after another making the process much faster. 

**Features**

**Automated Shopify Store Information Extraction**: The  script automatically navigates to a list of Shopify stores(Found by using this website to find all stores hosted by Shopify: [https://myip.ms](https://myip.ms/browse/sites/1/ownerID/376714/ownerIDii/)) and extracts the URLs of the Shopify stores and writes them to a CSV file.

**Contact Form Detection**: The second script navigates to each Shopify store, locates the contact page, and fills out the contact form with predefined data.

**Resilience to CAPTCHA and Errors**: Both scripts are resilient to CAPTCHAs and page load errors. If a CAPTCHA is detected, a sound will be played, and the script will wait for the user to manually complete the CAPTCHA.

**Technologies Used**

Python

Selenium WebDriver

BeautifulSoup4/

Tkinter/
/
CSV

**Getting Started**

Ensure you have Python and pip installed on your machine.

Clone the repository:

git clone https://github.com/deep-chill/shopify-contact-form-automator.git

Install the required Python packages:
pip install -r requirements.txt

Run script1.py to start the Shopify store navigation and information extraction process.

**Usage**

In script1.py, specify the range of pages to scrape in the line for page_number in range(300, 5000).

Run script1.py. The script will navigate to each page of a Shopify store list website, attempt to locate a table of Shopify store URLs, and save these URLs to a csv.

Run script2.py. The script will read the URLs from the csv, navigate to each Shopify store's contact page, and attempt to fill the contact form with predefined data.

Note: During both scripts, if a CAPTCHA or an error is encountered, a beep sound will be played and the script will pause until you manually resolve the issue and press the "Continue to next website" button.

**Contributing**

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

**Contact**

Feel free to reach out if you have any questions or if you want to discuss this project further.

