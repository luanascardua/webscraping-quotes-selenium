from selenium.webdriver.common.by import By


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
            print(quote.text)
            print(self.driver.find_element(*self.url).get_attribute('href'))
            self.i += 1
            print(author.text)
            print(tags.text)
            input('continuar')      
