# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# ブラウザのオプションを格納する変数をもらってきます。
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1280')

# ブラウザを起動する
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.instagram.com/explore/tags/cherryblossom/")

def scan_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("img"):
        print(tag["src"])

for i in range(10):
    driver.refresh()
    sleep(3)
    html = driver.page_source.encode('utf-8')
    scan_html(html)

driver.quit()
