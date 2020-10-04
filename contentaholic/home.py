from flask import (    
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from . import source
from source import Source

bp = Blueprint('home', __name__)

TMZ = Source('TMZ', 'https://tmz.com')
sources = [TMZ]

@bp.route('/')
def index():
    return render_template('index.html', sources=sources)