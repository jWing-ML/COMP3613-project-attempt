from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import db, User
import json
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from App.controllers import create_user

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup')
def index():
  return render_template('signup.html')

@signup_views.route('/signup', methods=['POST'])
def signup_post():

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('username used already')
        return render_template('signup.html')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    #new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    #new_user = create_user(username, password)
    newuser = create_user(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    flash('Sign UP sucessfully')
    return render_template('login.html')