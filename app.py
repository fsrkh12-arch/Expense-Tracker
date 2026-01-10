from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
import os

# Configure Flask app
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Secret key for sessions
app.secret_key = os.urandom(24)

# Configure session to use filesystem (instead of cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///expenses.db")

# Helper function to require login
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# =====================
# ROUTES
# =====================

@app.route("/")
@login_required
def index():
    """Show dashboard (expenses will go here later)"""
    user_id = session["user_id"]
    # Placeholder: later we’ll fetch expenses from database
    expenses = []
    return render_template("index.html", expenses=expenses)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register new user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        # Validate submission
        if not username or not password or not confirm:
            flash("Please fill out all fields")
            return redirect("/register")
        if password != confirm:
            flash("Passwords do not match")
            return redirect("/register")

        # Check if username exists
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            flash("Username already exists")
            return redirect("/register")

        # Hash password and insert user
        hash_pw = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pw)

        flash("Registered successfully! Please log in.")
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()  # Clear any existing session

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validate form submission
        if not username or not password:
            flash("Please enter both username and password")
            return redirect("/login")

        # Query database for user
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username or password")
            return redirect("/login")

        # Remember which user is logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    flash("Logged out successfully")
    return redirect("/login")


# =====================
# Run app
# =====================
if __name__ == "__main__":
    app.run(debug=True)
