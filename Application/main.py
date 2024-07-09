from flask import Flask, render_template, flash, request, url_for, session, redirect
from werkzeug.utils import secure_filename
from models import db, User
from forms import RegisterForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import os
import shutil


app = Flask(import_name=__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SESSION_FILE_DIR"] = "/tmp/flask_session/"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['UPLOAD_FOLDER'] = 'Application/static/images'

csrf = CSRFProtect(app)
Session(app)


db.init_app(app)
csrf.init_app(app)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)


@app.route('/users/')
def users():
    if session.get('username'):
        role = User.query.filter_by(
            username=session.get('username')).first().role
    else:
        role = 'user'

    sort_by = request.args.get('sort', 'username')
    sort_dir = request.args.get('sort_dir', 'asc')

    users = User.query.order_by(
        getattr(User, sort_by).asc() if sort_dir == 'asc' else getattr(
            User, sort_by).desc()
    ).all()

    context = {
        'title': 'Пользователи',
        'users': users,
        'role': role,
        'sort_by': sort_by,
        'sort_dir': sort_dir,
        'url': url_for(endpoint='index'),
    }
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def user(username):
    context = {
        'title': 'Пользователь {}'.format(username),
        'user': User.query.filter_by(username=username).first(),
    }
    return render_template('user.html', **context)


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
####################################################


@app.route('/activate/<token>')
def activate(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.status = 'active'
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return render_template('404.html'), 404


@app.route('/ban/<token>')
def ban(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.status = 'banned'
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return redirect(url_for('users'))


@app.route('/unban/<token>')
def unban(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.status = 'active'
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return redirect(url_for('users'))

####################################################


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('register.html', form=form)
    else:
        # if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Такой логин уже занят", category='error')
        elif existing_email:
            flash("Такая почта уже занята", category='error')
        elif password != form.confirm_password.data:
            flash("Пароли не совпадают", category='error')
        else:
            user = User(username=username, email=email, password=password,
                        avatar=f'static/images/{username}/avatar.jpg')
            db.session.add(user)
            db.session.commit()

            # создание /static/images/user/avatar.jpg
            file_path = os.path.join(
                'Application/static/images', username, 'avatar.jpg')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            shutil.copyfile(
                'Application/static/images/default_avatar.jpg', file_path)

            flash("Регистрация прошла успешно", category='success')
            session['username'] = username
            session['password'] = password
            session['email'] = email
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(
                username=username, password=password).first()
            if user:
                flash("Вы вошли в аккаунт", category='success')
                session['username'] = username
                session['password'] = password
                return redirect(url_for('index'))
            else:
                flash("Неверный логин или пароль", category='error')
        return render_template('login.html', form=form)


@app.route(rule='/logout/', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        del session['username']
        del session['password']
    flash(message="Вы вышли из аккаунта", category='info')
    return redirect(url_for(endpoint='index'))


@app.route('/delete/<token>')
def delete(token):
    user = User.query.filter_by(token=token).first()
    if user:
        db.session.delete(user)
        db.session.commit()

        try:
            shutil.rmtree(f'Application/static/images/{user.username}')
        except FileNotFoundError:
            pass

        return redirect(url_for('users'))
    else:
        return render_template('404.html'), 404


@app.route('/setadmin/<int:id>')
def setadmin(id):
    user = User.query.get(id)
    user.role = 'admin'
    db.session.commit()
    return redirect(url_for('users'))


@app.route('/setuser/<int:id>')
def setuser(id):
    user = User.query.get(id)
    user.role = 'user'
    db.session.commit()
    return redirect(url_for('users'))


@app.route('/createbots/')
def createbots():
    from secrets import token_hex
    for i in range(25):
        user = User(username=f'test{i}', email=f'test{i}@test.com',
                    password='123', token=token_hex(16))
        db.session.add(user)
        db.session.commit()

    return redirect(url_for('users'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(debug=True)
