# coding: UTF-8
from bs4 import BeautifulSoup
from time import sleep

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
        :rtype:     [{img_url: "", post_url: ""}]
        """

        self.driver.get(TagScraper.scrape_base_url + hashtag + "/")
        html = self.driver.page_source.encode('utf-8')
        return scan_html(html)

def scan_html(html):
    soup = BeautifulSoup(html, "html.parser")
    insta_posts = []
    for img_tag in soup.select("a div div img"):
        img_url = img_tag['src']
        post_url_path = img_tag.parent.parent.parent['href']
        post_url = "https://www.instagram.com" + post_url_path
        insta_posts.append({'img_url': img_url, 'post_url': post_url})
    return insta_posts
