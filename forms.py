from flask_wtf import FlaskForm
from wtforms.fields.simple import (
    PasswordField,
    SubmitField,
    StringField,
)
from wtforms.validators import Email, DataRequired, Length


class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Password should be at least %(min)d characters long",
            ),
        ],
    )
    submit = SubmitField(label="Log In")
