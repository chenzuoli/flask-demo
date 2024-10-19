from flask import render_template

from app.models.post import Post
from app.posts import bp


@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')
