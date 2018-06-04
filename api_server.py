# coding: UTF-8
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from bottle import get, run, request, abort

from tag_scraper import TagScraper

@get('/posts/<post_id>')
def get_post_by_id(post_id):
    return "WIP"

@get('/posts')
def get_posts():
    print("hoge")
    hashtag = request.query.get('hashtag')
    if hashtag is None:
        return abort(400, "you must set hashtag parameter")
    posts = TagScraper(hashtag).scrape()
    print(posts)
    return {'posts': posts}

def run_server(host, port):
    run(host = host, port = port, debug = True)
