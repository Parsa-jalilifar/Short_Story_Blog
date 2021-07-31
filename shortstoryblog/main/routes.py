from flask import Blueprint, render_template, url_for
from flask_login import login_required
from shortstoryblog.models import Post

main = Blueprint("main", __name__)

# posts = [
#     {
#         "author": "Shane Ransom",
#         "title": "Favorites",
#         "content": "I saw a tree and thought of you, or rather, thought of the way you see trees. I remembered when we walked through the Ramble in Central Park, a wild place in the center of a place wilder still, resplendent and emerald in the early summer sun. You stopped suddenly when you saw it. I remember how you cocked your head in appreciation, a tendril of hair escaped from behind your ear. You brushed it back with an unconscious ha...",
#         "date_posted": "Jan 13, 2021",
#         "image_file": "default.jpg",
#     },
#     {
#         "author": "Colleen",
#         "title": "Mary Sheehan",
#         "content": "Colleen is packing to leave for university. She folds her clothes into neat piles, her fair hair arranged in an artfully messy bun, with gold strands curling around her face. She packs her rolled up socks into the maze of groves left by the clothes piles. Her movements are thoughtful and tender, like she is tucking them into bed. I watch her from my quiet corner outside the door of her room, chewing on a hangnail. I am still wearing my pyjamas and I haven’t showered yet today. I stare at her, willing her to hea...",
#         "date_posted": "Jul 08, 2021 ",
#         "image_file": "default.jpg",
#     },
#     {
#         "author": "Rayhan Hidayat",
#         "title": "mie goreng",
#         "content": "I’d rather be asleep.I’d rather have ignored your request at my door, small and pleading and moist with youth. I’d rather the song of your furtive feet retreating as quickly as they’d come had been a stray breeze in the night, or the cackling melody of mating geckos. I’d rather have curled deeper into the naked mattress that carves brutal shapes into my spine, because sleep is something I don’t get enough of.Yet here I am, groping for a light switch in a kitchen that I spend more time inside than my own..",
#         "date_posted": "Jul 02, 2021 ",
#         "image_file": "default.jpg",
#     },
#     {
#         "author": "Tom Vandel",
#         "title": "The Men and the Lake",
#         "content": "The Men And The Lake We could talk about the storm. We could talk about the wind and waves. We could talk about the boat. We could talk about the life jackets. We could talk about the men and the lake. We could talk about why they went so far out from shore.",
#         "date_posted": "Jun 24, 2021 ",
#         "image_file": "default.jpg",
#     },
# ]


@main.route("/")
@main.route("/home")
@login_required
def home():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template("home.html", title="Home", posts=posts)
