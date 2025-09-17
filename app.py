from flask import Flask, render_template, request, redirect, url_for
from db import init_db
from user_service import register_user, list_users

app = Flask(__name__)

@app.route("/")
def index():
    users = list_users()
    return render_template("index.html", users=users)

@app.route("/register", methods=["GET", "POST"])
def register():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        age = request.form.get("age")

        try:
            age = int(age)
        except ValueError:
            age = None

        success, msg = register_user(username, email, age)
        message = msg
        if success:
            return redirect(url_for("index"))

    return render_template("register.html", message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
