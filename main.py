from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from scraping_quotes import Quotes


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--start-maximized')
chrome = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome, options=chrome_options)

driver.get('http://quotes.toscrape.com/')

quotes = Quotes(driver, i=1)
quotes.get_quotes()