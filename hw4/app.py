# HW4 - Art Institute of Chicago Search App
from api import search_art
# Home Route (/)
# 1. Create a Flask route for the homepage
# 2. Display home.html with a search form
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
# Results Route (/results)
@app.route("/results")
def results():
    keyword = request.args.get("author_search", "").strip()

    if not keyword:
        return render_template(
            "home.html",
            message="Please enter a search term."
        )
    artworks = search_art(keyword)
    return render_template(
        "results.html",
        artworks=artworks,
        keyword=keyword
    )
# 1. Get the search keyword from the form
# 2. Check if the keyword is empty
# 3. If empty, return home.html with a message
# 4. Call the search_art() function from api.py
# 5. Check if the API request failed
# 6. Check if the search returned no artworks
# 7. Handle missing artwork information
# 8. Display results.html with the artworks