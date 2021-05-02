from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required, current_user
from app.main import main
from app.models import User, Blog, Comment, Subscriber
from .forms import UpdateProfile, CreateBlog
from .. import db
from ..email import mail_message


@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.posted.desc()).limit(3).all()
    return render_template('index.html', blogs=blogs)


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


@main.route('/new_post', methods=['POST', 'GET'])
@login_required
def new_blog():
    subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user._get_current_object().id
        blog = Blog(title=title, content=content, user_id=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("New Blog Post", "email/new_blog", subscriber.email, blog=blog)
        return redirect(url_for('main.index'))
    flash('You Posted a new Blog')
    return render_template('newblog.html', form=form)


@main.route('/comment/<blog_id>', methods=['Post', 'GET'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment = request.form.get('newcomment')
    new_comment = Comment(comment=comment, user_id=current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    return redirect(url_for('main.blog', id=blog.id))


@main.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email=email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Archïtecture", "email/welcome_subscriber", new_subscriber.email,
                 new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
