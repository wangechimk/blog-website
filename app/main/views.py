from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required
from app.main import main
from app.models import User
from .forms import UpdateProfile
from .. import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile/<name>')
@login_required
def profile(name):
    user = User.query.filter_by(username=name).first()
    if user == None:
        abort(404)

    return render_template('profile/profile.html', user=user)


@main.route('/user/<name>/updateprofile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/updateprofile.html', form=form)
