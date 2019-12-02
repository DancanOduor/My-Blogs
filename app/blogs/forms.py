from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField( 'Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField( 'Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    body = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    body = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Submit")
