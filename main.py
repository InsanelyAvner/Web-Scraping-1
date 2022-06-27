from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


# Write code here
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)

headers = ["name", "distance", "mass", "radius"]
planet_datas = []


time.sleep(10)

def scrap():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    table = soup.find_all('table')[0]

    for tr_tags in table.find_all("tr"):
        td_tags = tr_tags.find_all("td")
        temp_list = []

        for index, td_tag in enumerate(td_tags):
            if index == 1:
                # temp_list.append(td_tag.a.string)
                try:
                    temp_list.append(td_tag.find("a").string)
                except:
                    temp_list.append(td_tag.string)
            elif index in [1, 3, 5, 6]:
                try:
                    temp_list.append(td_tag.contents[0].strip())
                except:
                    temp_list.append("")
        
        planet_datas.append(temp_list)
    
    # Create CSV file
    with open("scrapper_2.csv", "w") as f:
        writer = csv.writer(f)

        writer.writerow(headers)
        writer.writerows(planet_datas)
    
    print(planet_datas)
    
scrap()