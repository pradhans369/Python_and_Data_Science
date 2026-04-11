from flask import Flask, render_template, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# --------------------------------------------------------------------------------------------------------------------------
# page to receive html template
@app.route("/")
def home():
    return render_template("login.html")


# --------------------------------------------------------------------------------------------------------------------------
# page to receive user details
@app.route("/submit", methods=["POST"])
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
        return """
            <h2><u>INVALID / INCOMPLETE</u> LOGIN CREDENTIALS, try again...</h2>
"""


# --------------------------------------------------------------------------------------------------------------------------
# making a function for to check for student's topper status
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    # 1. Grab the username from memory
    Username = session.get('username')
    topper_status = request.form.get("is_topper")
    
    return render_template("profile.html", name=Username, topper=topper_status, subjects=['Math','English','Hindi'])


# --------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
