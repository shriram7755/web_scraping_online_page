# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:44:37 2023

@author: SHRI
"""

# # web scraping online page
# =============================================================================

from bs4 import BeautifulSoup as bs
import requests
link='https://sanjivanicoe.org.in/index.php/contact'
page=requests.get(link)
page
# response [200] it means connection is successfully established
# let us apply html parser
soup=bs(page.content,'html.parser')
soup
# now the text is clean but not upto expectation
# lets apply prettify method
print(soup.prettify())
# text is neat and clean
print(soup.children)
# finding all contents from
# first now
soup.find_all('p')[1].get_text()
# contents from 2nd row
soup.find_all('p')[2].get_text()
# finding text using class
soup.find_all('div',class_='table')
