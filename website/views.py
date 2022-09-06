from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website import db
from .models import Post

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    post = Post.query.all()
    return render_template('home.html', user=current_user, posts=post)
    # return render_template("home.html" , user=current_user)

@views.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')

        if len(text) < 1:
            flash('Post is too short!', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("create_post.html", user=current_user)