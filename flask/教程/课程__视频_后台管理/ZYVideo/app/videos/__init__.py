from flask import Blueprint 

video = Blueprint('videos',__name__)

from . import views