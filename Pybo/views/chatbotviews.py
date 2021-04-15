from flask import Blueprint, render_template, url_for, request, flash, session, g
from Pybo.models import User
from Pybo.forms import UserCreateForm, UserLoginForm
from datetime import datetime
from Pybo import db
from werkzeug.utils import redirect
import functools
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('chatbot', __name__, url_prefix='/chatbot')

@bp.route('/')
def chatbot():
    return render_template('chatbot/chatbot.html')