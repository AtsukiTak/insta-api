# coding: UTF-8
from bs4 import BeautifulSoup
from time import sleep
import re

class TagScraper:
    """
    A simple instagram tag scraper class. For now, I don't aim performance.
    """

    scrape_base_url = "https://www.instagram.com/explore/tags/"

    def __init__(self, driver):
        self.driver = driver

    def scrape(self, hashtag):
        """
        Fetch current information about instagram posts related to specified hashtag.

        # Warn
        This method takes around 3 seconds. Caller must take care about it.

        :return:    A list of instagram post dictionary.
        :rtype:     [{image_url: "", post_id: ""}]
        """

        self.driver.get(TagScraper.scrape_base_url + hashtag + "/")
        html = self.driver.page_source.encode('utf-8')
        return scan_html(html)

regex = re.compile(r'^/p/(.+)/')

def scan_html(html):
    soup = BeautifulSoup(html, "html.parser")
    insta_posts = []
    for img_tag in soup.select("a div div img"):
        img_url = img_tag['src']
        post_path = img_tag.parent.parent.parent['href']
        post_id = regex.match(post_path).group(1)
        insta_posts.append({'image_url': img_url, 'post_id': post_id})
    return insta_posts
