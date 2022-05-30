"""
Developer: @skywalkerSam
Purpose: Learning Web Scraping
Date: 12022.05.29.13:16
"""

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
print(res)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

links = soup.select(".titlelink")   # title link
votes = soup.select(".score")   # votes 


prt = soup.find("title")
print(prt)

prt2 = soup.find("a")
print(prt2)

prt3 = soup.findAll("a")
print(prt3)


