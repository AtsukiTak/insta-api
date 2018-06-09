# coding: UTF-8
from bs4 import BeautifulSoup
from time import sleep

class PostScraper:
    """
    A simple instagram post scraper class. For now, I don't aim performance.
    """

    scrape_base_url = "https://www.instagram.com/p/"

    def __init__(self, driver):
        self.driver = driver
        self.is_first_time = True

    def scrape(self, post_id):
        """
        Fetch an information about instagram posts specified by id.

        # Warn
        This method takes around 3 seconds. Caller must take care about it.

        :return:    An instagram post dictionary.
        :rtype:     {user_name: ""}
        """

        self.driver.get(PostScraper.scrape_base_url + post_id + "/")
        html = self.driver.page_source.encode('utf-8')
        return scan_html(html)

def scan_html(html):
    soup = BeautifulSoup(html, "html.parser")
    uname = soup.select_one("header div div div a").string
    image_url = soup.select("img")[1]['src']
    return {"user_name": uname, "image_url": image_url}
