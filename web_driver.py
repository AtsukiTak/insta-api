# coding: UTF-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1280')
    return webdriver.Chrome(options=options)
