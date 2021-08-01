from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from shortstoryblog import db
from shortstoryblog.models import Post
from shortstoryblog.posts.forms import PostForm


posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template(
        "create_post.html", title="New Post", form=form, legend="Create New Post"
    )
