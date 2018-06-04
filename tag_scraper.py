# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TagScraper:
    """
    A simple instagram scraper class. For now, I don't aim performance.
    """

    scrape_base_url = "https://www.instagram.com/explore/tags/"

    def __init__(self, hashtag):
        self.driver = init_driver()
        self.is_first_time = True
        self.hashtag = hashtag

    def scrape(self):
        """
        Fetch current information about instagram images related to specified hashtag.

        This method does 2 steps.
        1. load corresponding instagram page
        3. extract image information from loaded page

        # Warn
        This method takes around 3 seconds. Caller must take care about it.

        :return:    A list of instagram post dictionary.
        :rtype:     [{img_url: "", post_url: ""}]
        """

        self.driver.get(TagScraper.scrape_base_url + self.hashtag)
        html = self.driver.page_source.encode('utf-8')
        self.driver.close()
        return scan_html(html)

def init_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1280')
    return webdriver.Chrome(options=options)

def scan_html(html):
    soup = BeautifulSoup(html, "html.parser")
    insta_posts = []
    for img_tag in soup.select("a div div img"):
        img_url = img_tag['src']
        post_url_path = img_tag.parent.parent.parent['href']
        post_url = "https://www.instagram.com" + post_url_path
        insta_posts.append({'img_url': img_url, 'post_url': post_url})
    return insta_posts
