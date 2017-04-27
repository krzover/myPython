from flask import Blueprint 

teacher = Blueprint('teachers',__name__)

from . import views 