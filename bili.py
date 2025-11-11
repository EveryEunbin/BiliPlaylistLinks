from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import csv

options = Options()
options.add_argument("--headless")

url = 'https://www.bilibili.tv/th/video/4789988705960448?bstar_from=bstar-web.ugc-video-detail.playlist.all'

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
        short_title = current_title.replace(" - BiliBili", "")
        current_url = driver.current_url
        short_url = current_url.replace("?bstar_from=bstar-web.ugc-video-detail.playlist.all", "")
        writer.writerow({'title': short_title, 'link': short_url})
        print(short_title, short_url)

driver.quit()