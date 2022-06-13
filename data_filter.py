import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
PATH = Service("C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service = PATH)

competitions_read = pd.read_csv("raw_datasets\competitions.csv")
competitions_read.head()
url = [competitions_read.loc[competitions_read.domestic_league_code == x].iloc[0,7] 
       for x in ["GB1", "IT1", "ES1", "FR1", "L1"]]

driver.get(url[0])
search = driver.find_element("tag name", "tbody").text

print(driver.title)

driver.close()