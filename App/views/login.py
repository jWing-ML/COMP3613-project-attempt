from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import db, User
import json
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from App.controllers import authenticate
from flask_login import login_user

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/login')
def index():
  return render_template('login.html')

@login_views.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('cbox') else False

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
      flash('Please check your login details and try again.')
      return render_template('login.html') # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    
    login_user(user, remember= remember)
    flash('LogIn Sucessful')
    return render_template('profile.html', user=user)

  
