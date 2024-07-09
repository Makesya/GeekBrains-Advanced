from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[
                           DataRequired(), Length(min=4, max=20)], render_kw={'class': 'form-control mb-3', 'placeholder': 'Логин'})
    password = StringField('Пароль', validators=[
                           DataRequired(), Length(min=6, max=20)], render_kw={'class': 'form-control mb-3', 'placeholder': 'Пароль'})
    confirm_password = StringField('Повторите пароль', validators=[
                                   DataRequired()], render_kw={'class': 'form-control mb-3', 'placeholder': 'Повторите пароль'})
    email = StringField('Почта', validators=[
                        DataRequired(), Email(), Length(min=6, max=50)], render_kw={'class': 'form-control mb-3', 'placeholder': 'Почта'})
    submit = SubmitField('Зарегистрироваться', render_kw={
                         'class': 'btn btn-primary mb-3'})


class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={
                           'class': 'form-control mb-3', 'placeholder': 'Логин'})
    password = StringField('Password', validators=[DataRequired()], render_kw={
                           'class': 'form-control mb-3', 'placeholder': 'Пароль', 'type': 'password'})
    submit = SubmitField('Войти', render_kw={
                         'class': 'btn btn-primary mb-3'})
