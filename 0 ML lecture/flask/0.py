from flask import Flask, request

# now we have to make an object
app = Flask(__name__)

# http://127.0.0.1:5000

# --------------------------------------------------------------------------------------------------------------------------
# creating pages
@app.route("/")
def home():
    return "Gracias ! this is the home page"

# --------------------------------------------------------------------------------------------------------------------------
# this is about page
@app.route("/about")
def about():
    text = """This is the about page<br>
    We are learning flask
    """
    return text

# --------------------------------------------------------------------------------------------------------------------------
# this is contact page
@app.route("/contact")
def contact():
    text = """This is the contact page.<br>
    Phone : 7848884936<br>
    E-Mail : biswajeetpradhan36933@gmail.com / biswajeet3838@gmial.com"""
    return text

# make sure that route name always unique and readable route names
 
# --------------------------------------------------------------------------------------------------------------------------
#  making get and post
@app.route("/submit", methods=['GET','POST'])       # make sure both GET and POST are in upper case
def submit():
    if request.method == 'POST':
        return 'YOU SENT DATA<br><br>[THIS IS AN EXAMPLE OF POST]'
    else:
        # On a normal GET request, show an HTML form with a submit button
        return '''
        <form method="POST" action="/submit">
            <button type="submit">Click to send a POST request!</button>
        </form>
        '''
@app.route("/submit2", methods=['GET','POST'])       # make sure both GET and POST are in upper case
def submit2():
    if request.method == 'POST':
        return 'YOU SENT DATA'
    else:
        text = """YOU DIDN'T SEND ANY DATA, YOU ARE JUST VIEWING THE WEBSITE<br><br>
        [THIS IS AN EXAMPLE OF GET]"""
        return text

# --------------------------------------------------------------------------------------------------------------------------









# --------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
