from flask import Flask, render_template, request, redirect, url_for, flash, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# --------------------------------------------------------------------------------------------------------------------------
# page to receive html template
@app.route("/")
def home():
    return render_template("login.html")


# --------------------------------------------------------------------------------------------------------------------------
# page to receive user details
@app.route("/submit", methods=["GET","POST"])
def login():
    Username = request.form.get("username")
    E_mail = request.form.get("email")
    Password = request.form.get("password")

    # making session to use the received details across different routes
    session['username'] = Username
    session['email'] = E_mail
    session['password'] = Password


    # making a dictionary for storing the details for admins
    admins = {
        'name': ['Biswajeet Pradhan', 'ashura'],
        'email': ['pdn@gmail.com', 'ashura@gmail.com']
    }

    # this condition is for admins only
    if Username in admins['name'] and E_mail in admins['email']:
        return f"<h2>welcome {Username} (Admin)</h2>"
     
    # this condition is for normal users
    elif Username and E_mail and Password:
        return render_template("welcome.html", name=Username)
    
    # this condition is for invalid credentials
    else:
        return render_template("submit.html")


# --------------------------------------------------------------------------------------------------------------------------
# making a function for to check for student's topper status
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    Username = session.get('username')
    topper_status = request.form.get("is_topper")
    

    if topper_status:
        session['is_topper'] = topper_status
    else:
        topper_status = session.get('is_topper')        # here session.get() will only return "None"

    return render_template("profile.html", name=Username, topper=topper_status, subjects=['Math','English','Hindi'])


# --------------------------------------------------------------------------------------------------------------------------

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    # We grab the user info from the session because the feedback form doesn't actually have a username input!
    Username = session.get('username', 'User')
    topper_status = session.get('is_topper')

    # ONLY trigger the flash message IF they actually clicked the submit button!
    if request.method == 'POST':
        flash(f"Thanks {Username} for your feedback", "success")
        return redirect(url_for('home'))
        
    return render_template("feedback.html", name=Username, topper=topper_status)


# --------------------------------------------------------------------------------------------------------------------------

@app.route("/check_data")
def check_data():
    # We grab EVERYTHING from the session to show it on the page
    all_data = dict(session)
    return render_template("check_data.html", data=all_data)


# --------------------------------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
