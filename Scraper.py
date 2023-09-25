# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import time
from datetime import datetime
from asinGenerator import canadian, american  # Not sure what this does, as its functionality is not given

class Scrape:
    def __init__(self, url):
        # Initialize Selenium Webdriver and BeautifulSoup 
        self.PATH = "/Users/main/desktop/code/scraping/chromedriver_PATH_for_selenium_ref/chromedriver"
        self.usAsins = american()  # Not used in the provided code
        self.chrome_options = Options()
        self.chrome_options.headless = True
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
        self.actions = ActionChains(self.driver)
        self.url = url
        # Initialize data storage lists
        self.product_name = []
        self.reviews = []
        self.zipped_list = []
        self.rating_list = []

        # Try to get information, and finally, return data
        try:
            self.get_info()
        finally:
            self.return_data()

    def get_info(self):
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        product_name = None

        # Extract initial product and review data
        try:
            product_name = self.driver.find_element_by_css_selector("#productTitle").text
            self.driver.find_element_by_css_selector("#reviews-medley-footer .a-text-bold").click()
            self.extract_reviews_and_ratings(product_name)
        except:
            print("Some error at the start occurred")

        # Extract more review data from subsequent pages
        for _ in range(6):  # Assuming the code tries to scrape 6 pages
            try:
                self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
                time.sleep(1)
                self.extract_reviews_and_ratings(product_name)
                print('success')
            except:
                print("It didn't work")
        
        # Close the driver
        self.driver.close()

    def extract_reviews_and_ratings(self, product_name):
        """Utility function to extract reviews and ratings from the current page."""
        review_elements = self.driver.find_elements_by_css_selector(".review-text-content span")
        rating_elements = self.soup.find_all('i', {'data-hook': 'review-star-rating'})
        
        # Process ratings
        if not rating_elements:
            self.rating_list.extend(["Failed to grab rating"] * len(review_elements))
        for rate in rating_elements:
            self.rating_list.append(rate.span.text.strip() or 'Rating failed to grab')
        
        # Process reviews
        for review in review_elements:
            self.reviews.append(review.text)
        
        # Add product names for each review
        self.product_name.extend([product_name] * len(review_elements))

    def return_data(self):
        """Save scraped data to an Excel file."""
        wb = load_workbook('data.xlsx')
        ws = wb.active
        self.zipped_list = list(zip(self.product_name, self.rating_list, self.reviews))
        for data_row in self.zipped_list:
            ws.append(data_row)
        wb.save('data.xlsx')
