# coding: UTF-8
from bottle import get, Bottle
from paste import httpserver
from instalooter.looters import HashtagLooter, PostLooter

from itertools import islice
import os

app = Bottle()

@app.get('/hashtags/<hashtag>')
def get_hashtag(hashtag):
    print("get hashtag : %s" % hashtag)
    looter = HashtagLooter(hashtag)
    medias = islice(looter.medias(), 100)
    res = list(map(media_to_dict, medias))
    return { "res": res }

def media_to_dict(media):
    dic = {
        "id": media["shortcode"],
        "image_url": media["display_url"],
        "user_id": media["owner"]["id"],
    }
    return dic


@app.get('/posts/<post_id>')
def get_post(post_id):
    print("get post : %s" % post_id)
    looter = PostLooter(post_id)
    post = looter.get_post_info(post_id)
    return post

def run_server():
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", "8000")
    debug = os.getenv("DEBUG", True)
    httpserver.serve(app, host = host, port = port)

run_server()
