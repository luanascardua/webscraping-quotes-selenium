<h1 align="center">
  webscraping quotes selenium
</h1>

## About

Percorre todas as páginas do site [Quotes to Scrape](http://quotes.toscrape.com/) para armazenar os dados de cada citação.
### output
As informaçãos são gravadas num arquivo `.json`, gerado a partir da execução do programa, seguindo a estrutura do dicionário: 
``` python
{
    "quote": quote,
    "author": {
         "name":author,
         "url":url
     },
    "tags":[tags]
}

```

## Tools
- [Python](https://docs.python.org/3/)
- [Selenium Framework](https://www.selenium.dev/documentation/)
    - **webdriver**: utilizado chrome driver para interação com browser
        - `webdriver-manager`: realiza o download do driver automaticamente de acordo com a versão instalada do chrome
        
 ## execute
 ```
 python main.py
 ```
