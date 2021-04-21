from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from asinGenerator import canadian, american
from bs4 import BeautifulSoup
import time
from openpyxl import load_workbook
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url):
        self.PATH = "/Users/main/desktop/code/scraping/chromedriver_PATH_for_selenium_ref/chromedriver"
        self.usAsins = american()
        self.chrome_options = Options()
        self.chrome_options.headless = True
        self.chrome_options.add_argument = ("--disable-extensions")
        self.chrome_options.add_argument = ("--disable-gpu")
        self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
        self.actions = ActionChains(self.driver)
        self.url = url
        self.product_name = []
        self.reviews = []
        self.zipped_list = []
        self.rating_list = []
     
  
        try:
            self.get_info()
        finally:
            pass
            self.return_data()
    

        
    

    def get_info(self):
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        try:
            product_name = self.driver.find_element_by_css_selector("#productTitle").text
            self.driver.find_element_by_css_selector("#reviews-medley-footer .a-text-bold").click()
            review_1 = self.driver.find_elements_by_css_selector(".review-text-content span")
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            length = int(len(review_1))
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab')  
            for i in review_1:
                self.reviews.append(i.text)  
        except:
            pass 
            print("Some error at the start occured")

        try:
            self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
            time.sleep(1)
            review_2 = self.driver.find_elements_by_css_selector(".review-text-content span")
      
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            length = int(len(review_2))
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab')    
 
        
            for i in review_2:
                self.reviews.append(i.text)
                    
            print('success')
            
        except:
            pass
            print("It didnt work")   
        
        try:
            self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
            time.sleep(1)
            review_2 = self.driver.find_elements_by_css_selector(".review-text-content span")
            length = int(len(review_2))
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for i in review_2:
                self.reviews.append(i.text)

            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab') 

   
            print('success')
            
        except:
            pass
            print("It didnt work")  
       
        
        try:
            self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
            time.sleep(1)
            review_2 = self.driver.find_elements_by_css_selector(".review-text-content span")
            length = int(len(review_2))
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for i in review_2:
                print(rate.text)
                self.reviews.append(i.text)
  
            
            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab')   
        
            print('success')
            
        except:
            pass
            print("It didnt work") 

        try:
            self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
            time.sleep(1)
            review_2 = self.driver.find_elements_by_css_selector(".review-text-content span")
            length = int(len(review_2))
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for i in review_2:
                self.reviews.append(i.text)
        
            
            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab')    
        
            print('success')
            
        except:
            pass
            print("It didnt work")  

        try:
            self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
            time.sleep(1)
            review_2 = self.driver.find_elements_by_css_selector(".review-text-content span")
            length = int(len(review_2))
            rating = self.soup.find_all('i', {'data-hook':'review-star-rating'})
            if not rating:
                for i in range(length):
                    self.rating_list.append("Failed to grab rating")
            for i in review_2:
                self.reviews.append(i.text)
      
            for rate in rating:
                print(rate.span.text.strip())
                self.rating_list.append(rate.span.text.strip())
                if not rate:
                    self.rating_list.append('Rating failed to grab')     
           
            print('success')
            
        except:
            pass
            print("It didnt work")  
 
        
      
        number = int(len(self.reviews))
        for i in range(number):
            self.product_name.append(product_name)  

        self.zipped_list = list(zip(self.product_name, self.rating_list, self.reviews))
        print(self.zipped_list)

        self.driver.close()
    
    

    def return_data(self):
        
        wb = load_workbook('data.xlsx')
        ws = wb.active
        for i in self.zipped_list:
            ws.append(i)
        
        wb.save('data.xlsx')
        



    
        