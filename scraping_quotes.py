from selenium.webdriver.common.by import By
import json

class Quotes:

    def __init__(self, driver, i):
        self.driver = driver
        self.i = i

        self.quote = By.CLASS_NAME, 'text'
        self.author = By.CLASS_NAME, 'author'
        self.tags = By.CLASS_NAME, 'tags'
        self.url = By.XPATH, f'/html/body/div/div[2]/div[1]/div[{i}]/span[2]/a'

        self.btn_next_page = By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.col-md-8 > nav > ul > li.next > a'                               
       
                                        
    def get_quotes(self):   
    
        while 'Next' in self.driver.page_source:
            for quotes, author, tags in zip(self.driver.find_elements(*self.quote), 
                                            self.driver.find_elements(*self.author),
                                            self.driver.find_elements(*self.tags)):
                url = self.driver.find_element(*self.url).get_attribute('href')
                self.i += 1
            
                tags = str(tags.text).split(' ')
                if 'Tags:' in tags:
                    tags.remove('Tags:')
                
                dict_quotes = {
                "quote": quotes.text,
                "author": {
                    "name":author.text,
                    "url":url
                },
                "tags":tags
            }
                print(f'{dict_quotes}\n')
                self.write_json(dict_quotes)

            self.driver.find_element(*self.btn_next_page).click()      

    def write_json(self, dict):
        with open('quotes.json', 'a') as f:
            return json.dump(dict, f, indent=4, separators=(',', ':'))
