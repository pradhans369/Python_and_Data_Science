from flask import Flask, request, redirect, url_for, session, Response

# now we have to make an object
app = Flask(__name__)
app.secret_key = "supersecret"      # keeps the session key secret
# without the secret key, flask will never allow you use session


# http://127.0.0.1:5000

# --------------------------------------------------------------------------------------------------------------------------
# login function for user
@app.route("/", methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session['user'] = username             # storing the username
            return redirect(url_for('welcome'))
        else:
            return Response("INVALID CREDENTIALS. Try Again", mimetype="text/plain")    

    return """
        <h2>Login Page</h2>
        <form method="POST">
            Username : <input type='text' name='username'><br>
            Password : <input type='text' name='password'><br>
        <input type="submit" value="Login">
        </form>    


"""
# --------------------------------------------------------------------------------------------------------------------------
# welcoming and logout function for user
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
            <h2>Welcome, {session['user']}</h2><br>
            
            <form action="{url_for('logout')}">
                <input type='submit' value='Logout'>
            </form>
"""
    return redirect(url_for("login"))
# hred = hyper reference

# --------------------------------------------------------------------------------------------------------------------------
# making a funtion to remove the user key from the session after the user logsout
@app.route("/logout")
def logout():
    session.pop('user', None)     # removes the user as he/she logsout
    return redirect(url_for("login"))
 
# --------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------









# --------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
