from selenium.webdriver.common.by import By
import json

class Quotes:

    def __init__(self, driver, i):
        self.driver = driver
        self.i = i

        self.quotes =  driver.find_elements(By.CLASS_NAME, 'text')
        self.author = driver.find_elements(By.CLASS_NAME, 'author')
        self.tags = driver.find_elements(By.CLASS_NAME, 'tags') 
        self.url = By.XPATH, f'/html/body/div/div[2]/div[1]/div[{i}]/span[2]/a'

    def get_quotes(self):   
    
        for quote, author, tags in zip(self.quotes, self.author, self.tags):
            url = self.driver.find_element(*self.url).get_attribute('href')
            tags = tags.text
            tags = str(tags).split(' ')
            self.i += 1
           
            dict_quotes = {
                "quote": quote.text,
                "author": {
                    "name":author.text,
                    "url":url
                },
                "tags":tags
            }
            print(dict_quotes)
            self.write_json(dict_quotes)
            #input('continuar')   

    def write_json(self, dict):
        with open('quotes.json', 'a') as f:
            return json.dump(dict, f, indent=4, separators=(',', ':'))
