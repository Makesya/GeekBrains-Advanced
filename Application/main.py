from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect, secure_filename
from models import db, User
from forms import RegisterForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(import_name=__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
csrf_token = CSRFProtect(app)


@app.route('/')
def index():
    users = User.query.all()
    context = {
        'title': 'Главная',
        'users': users
    }
    return render_template('index.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if not username or not email or not password:
            flash('Заполните все поля')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        return render_template('register.html', form=form)


@app.route('/tasks/')
def tasks():
    context = {
        'title': 'Задачи',
    }
    return render_template('tasks.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'О сервере',
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
