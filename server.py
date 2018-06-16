# coding: UTF-8
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from bottle import get, run, request, abort
import os

from tag_scraper import TagScraper
from post_scraper import PostScraper
from web_driver import init_driver

driver = init_driver()

@get('/posts/<post_id>')
def get_post_by_id(post_id):
    post = PostScraper(driver).scrape(post_id)
    post['post_id'] = post_id
    return post

@get('/posts')
def get_posts():
    hashtag = request.query.get('hashtag')
    if hashtag is None:
        return abort(400, "you must set hashtag parameter")
    posts = TagScraper(driver).scrape(hashtag)
    return {'posts': posts}

def run_server():
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", "8000")
    debug = os.getenv("DEBUG", True)
    run(host = host, port = port, debug = debug)

run_server()
