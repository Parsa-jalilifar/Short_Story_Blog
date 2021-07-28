from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

posts = [
    {
        "author": "Shane Ransom",
        "title": "Favorites",
        "content": "I saw a tree and thought of you, or rather, thought of the way you see trees. I remembered when we walked through the Ramble in Central Park, a wild place in the center of a place wilder still, resplendent and emerald in the early summer sun. You stopped suddenly when you saw it. I remember how you cocked your head in appreciation, a tendril of hair escaped from behind your ear. You brushed it back with an unconscious ha...",
        "date_posted": "Jan 13, 2021",
        "image_file": "default.jpg",
    }
]


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title="Home", posts=posts)
