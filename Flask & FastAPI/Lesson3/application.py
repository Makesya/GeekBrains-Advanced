from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post, Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content, author_id=1)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/')
def index():
    posts = Post.query.all()

    return render_template('index.html', title="Main", posts=posts)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Database was created")


if __name__ == '__main__':
    app.run(debug=True)
