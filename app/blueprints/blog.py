from os import path
from flask import json, request, Blueprint

blog_bp = Blueprint('blog', __name__)


def getPosts():
    # load json seed of post objects
    SITE_ROOT = path.abspath(path.dirname(path.dirname(__file__)))
    json_url = path.join(SITE_ROOT, "seed.json")

    return json.load(open(json_url))


@blog_bp.route('/api/posts/')
def posts():
    if request.method == 'GET':
        return getPosts()


@blog_bp.route('/api/posts/<string:slug>')
def post(slug):
    data = getPosts()
    posts = data["posts"]
    # lambda = anonymous function can take any number of arguments, but can only have one expression
    singlePost = filter(lambda post: post['slug'] == slug, posts)

    return list(singlePost)
