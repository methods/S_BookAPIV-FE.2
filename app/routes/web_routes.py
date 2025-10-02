"""
Routes for serving user-facing web pages.
"""

from flask import Blueprint, render_template

# Blueprint keeps routes organized
web_bp = Blueprint("web_bp", __name__)


@web_bp.route("/", methods=["GET"])
def index():
    """Serves the home page."""
    # For now, shows the books list as the home page
    return render_template("books.html")


@web_bp.route("/show-books", methods=["GET"])
def show_books_page():
    """Serves the page that lists all books."""
    # The actual data fetching happens via JavaScript in the template
    return render_template("books.html")
