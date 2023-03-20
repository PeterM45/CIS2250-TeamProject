#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

def code_scrape():
    url = "https://opendata.ehealthsask.ca/MicroStrategyPublic/asp/Main.aspx"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    print(doc.prettify())
    
    #res = doc.find_all(string = "2023")
    res = doc.find_all("div", class_="mstrmojo-progress")
    print(res)
    #print(results)
    #scrape_output = open('Output' + ".html", 'w+', encoding='utf-8')
    #scrape_output.write('\n')
    #scrape_output.write(results)
    #scrape_output.close()
    #print("Scraped to output file!")

code_scrape()