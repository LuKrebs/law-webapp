from laracunha import app, db
from flask import redirect, render_template, request, url_for, session

from home.models import History, Lawyer, Link, Area, Description


@app.route("/", methods=["GET"])
def home():
    return render_template('home/home.html')


@app.route("/about-us", methods=["GET"])
def about_us():
    return "Sobre nós"


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
