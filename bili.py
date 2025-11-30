from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import csv
import json

options = Options()
options.add_argument("--headless")

url = 'https://www.bilibili.tv/en/video/4795098891818496'

driver = webdriver.Firefox(options=options)
driver.get(url)
print(driver.title)
time.sleep(2)

with open('links.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    links = driver.find_elements(By.CSS_SELECTOR, ".playlist-card")
    for link in links:
        driver.execute_script("arguments[0].click();", link)
        time.sleep(5)
        current_title = driver.title
        short_title = current_title.replace(" - BiliBili", "").replace(" ", "_").replace(",","")
        current_url = driver.current_url
        short_url = current_url.replace("?bstar_from=bstar-web.ugc-video-detail.playlist.all", "")
        writer.writerow({'title': short_title, 'link': short_url})
        print(short_title, short_url)

driver.quit()

with open('links.csv', mode='r', newline='') as csvfile:
    data = list(csv.DictReader(csvfile))

with open('links.json', mode='w') as jsonfile:
    json.dump(data, jsonfile, indent=4, ensure_ascii=False)
