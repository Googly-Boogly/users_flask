from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    return render_template("Read.html", users = User.get_all())

@app.route("/create")
def create():
    # call the get all classmethod to get all friends
    return render_template("Create.html", )

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    print(data)
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)