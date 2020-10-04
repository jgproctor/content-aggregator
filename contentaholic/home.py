from flask import (    
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from contentaholic.source import Source

bp = Blueprint('home', __name__)

Tmz = Source('TMZ', 'https://tmz.com')
medium = Source('Medium', 'https://medium.com')
reddit = Source('Reddit', 'https://reddit.com')
sources = [Tmz, medium, reddit]

@bp.route('/')
def index():
    return render_template('index.html', sources=sources)
