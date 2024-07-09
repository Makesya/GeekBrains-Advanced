from flask import Flask, render_template, flash, request, url_for, session, redirect, abort
from werkzeug.utils import secure_filename
from models import db, User, SocialNetworks
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

csrf = CSRFProtect(app)
Session(app)


db.init_app(app)
csrf.init_app(app)


@app.context_processor
def inject_user():
    user = User.query.filter_by(username=session.get('username')).first()
    return dict(user=user)


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
    user = User.query.filter_by(username=username).first()

    social = SocialNetworks.query.filter_by(user_id=user.id).all()
    print(social)
    context = {
        'title': 'Пользователь {}'.format(username),
        'user': user,
        'social': social
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


@app.route('/deactivate/<token>')
def deactivate(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.status = 'unactive'
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

            images_folder = os.path.join('Application/static/images', username)
            if not os.path.exists(images_folder):
                os.makedirs(images_folder)
            file_path = os.path.join(
                images_folder, 'avatar.jpg')
            default_avatar_path = 'Application/static/images/default_avatar.jpg'
            shutil.copyfile(default_avatar_path, file_path)

            user = User(username=username, email=email, password=password,
                        avatar=f'/static/images/{username}/avatar.jpg')
            db.session.add(user)
            db.session.commit()

            # создание /static/images/user/avatar.jpg

            role = user.role

            flash("Регистрация прошла успешно", category='success')
            session['username'] = username
            session['password'] = password
            session['email'] = email
            session['role'] = role
            session['avatar'] = user.avatar
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
                session['role'] = user.role
                session['avatar'] = user.avatar
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


@app.route('/set/<int:id>/<string:role>')
def setadmin(id, role):
    user = User.query.get(id)
    user.role = role
    db.session.commit()
    return redirect(url_for('users'))


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if not session.get('username'):
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('edit.html')

    user = User.query.filter_by(username=session.get('username')).first()
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            user_folder = os.path.join(
                app.root_path, 'static', 'images', user.username)

            if not os.path.exists(user_folder):
                os.makedirs(user_folder)
            file_path = os.path.join(user_folder, filename)
            file.save(file_path)  # Теперь file - это объект файла, а не строка
            user.avatar = f'/static/images/{user.username}/{filename}'
            db.session.commit()
            session['avatar'] = user.avatar
        else:
            flash("No file provided for upload.", category='info')

    return redirect(url_for('edit'))


@app.route('/createbots/')
def createbots():
    from uuid import uuid4
    for i in range(25):
        user = User(username=f'test{i}', email=f'test{i}@test.com',
                    password='123', token=uuid4().hex)
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
