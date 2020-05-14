from flask import Flask, render_template, request, redirect, url_for
import re

# create the application object
app = Flask(__name__)


# importing regular expression for validation of email
def validateEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False


# I used r' for the pattern to be raw format.

# home decorator
@app.route("/")
def home():
    return render_template('success.html')


# using decorators to link the function to a URL
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if validateEmail(request.form['email']) != False and request.form['email'] and request.form[
            'myPassword'] is not "":
            return redirect(url_for('home'))
        else:
            error = "You have entered invalid credentials. Please try again."

    return render_template('login.html', error=error)
