from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
# Secret key is required for CSRF protection in Flask-WTF
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# making a form for login page
class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="name cannot be empty")])
    email = StringField("Email", validators=[DataRequired(message="message cannot be empty"), Email(message="not a valid email")])
    password = PasswordField("Password", validators=[DataRequired(message="password cannot be empty"), Length(min=8)])
    submit = SubmitField("Register")

# ----------------------------------------------------------------------------------------------------
@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        temp_name = form.name.data
        temp_email = form.email.data

        flash(f'Account created for {temp_name} [{temp_email}] !', 'success')
        return redirect(url_for('register'))
    return render_template('2_register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
