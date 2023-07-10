from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length
# from flask_wtf.file import FileField, FileRequired


class ContactForm(FlaskForm):
    email=StringField(label='Email',validators=[DataRequired(),Email("Invalid email address")])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=8,message="Password field must be 8 letters")])
    # photo = FileField(validators=[FileRequired()])
    submit=SubmitField(label='Login')

