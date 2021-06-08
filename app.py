import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Display home page 
@app.route("/")
@app.route("/home")
def home():
    #Check if there is a user in session 
    if "user" in session:
        user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        return render_template("index.html", user=user)
    else:
        return render_template("index.html")


# View club books
@app.route("/club_picks")
def club_picks():
    club_picks = mongo.db.club_picks.find()
    return render_template("club_picks.html")


# Sign up page 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username already exists in the database 
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("your_picks", username=session["user"]))

    return render_template("register.html")


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "your_picks", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/your_picks/<username>", methods=["GET", "POST"])
def your_picks(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("your_picks.html", username=username)

    return redirect(url_for("login"))



@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        your_picks = {
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "img_url": request.form.get("img_url"),
            "buy_url": request.form.get("buy_url"),
            "synopsis": request.form.get("synopsis"),
            "your_review": request.form.get("your_review"),
            "created_by": session["user"]
        }
        mongo.db.your_picks.insert_one(your_picks)
        flash("Book Successfully Added")
        return redirect(url_for("your_picks"))

    return render_template("add_book.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

