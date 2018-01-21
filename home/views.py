from laracunha import app, db
from flask import redirect, render_template, request, url_for, session

from home.models import History, Lawyer, Link, Area, Description

from helpers import get_history


@app.route("/", methods=["GET"])
def home():
    history = get_history()
    return render_template('home/pages/home.html', history=history)


@app.route("/about-us", methods=["GET"])
def about_us():
    history = get_history()
    return render_template('home/pages/about_us.html', history=history)


@app.route("/team", methods=["GET"])
def team():
    return "Equipe"


@app.route("/areas", methods=["GET"])
def areas():
    return "Áreas"


@app.route("/links", methods=["GET"])
def links():
    return "Links"


@app.route("/contact", methods=["GET"])
def contact():
    return "Contato"
