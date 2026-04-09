from flask import Flask

# now we have to make an object
app = Flask(__name__)

# http://127.0.0.1:5000

# creating pages
@app.route("/")
def home():
    return "Gracias ! this is the home page"

# this is about page
@app.route("/about")
def about():
    text = """This is the about page<br>
    We are learning flask
    """
    return text

# this is contact page
@app.route("/contact")
def contact():
    text = """This is the contact page.<br>
    Phone : 7848884936<br>
    E-Mail : biswajeetpradhan36933@gmail.com / biswajeet3838@gmial.com"""
    return text

# make sure that route name always unique and readable route names
 



# -------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
