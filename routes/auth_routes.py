from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask_bcrypt import Bcrypt

from utils.db_connection import get_db
from models.user_model import User


auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


# ==============================
# Landing Page
# ==============================

@auth_bp.route("/")
def landing():
    return render_template("landing.html")


# ==============================
# Sign In
# ==============================

@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        cursor = db.connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        if user:

            if bcrypt.check_password_hash(user["password"], password):

                user_obj = User(user)
                login_user(user_obj)

                return redirect(url_for("dashboard.dashboard"))

            else:
                flash("Incorrect password.")

        else:
            flash("Account not found. Please sign up first.")

    return render_template("signin.html")


# ==============================
# Sign Up
# ==============================

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        db = get_db()
        cursor = db.connection.cursor()

        # Check if user already exists
        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            flash("Email already registered. Please sign in.")
            return redirect(url_for("auth.signin"))

        # Insert new user
        cursor.execute(
            """
            INSERT INTO users (full_name, email, password, is_verified)
            VALUES (%s, %s, %s, TRUE)
            """,
            (full_name, email, hashed_password)
        )

        db.connection.commit()

        flash("Account created successfully. Please sign in.")

        return redirect(url_for("auth.signin"))

    return render_template("signup.html")


# ==============================
# Logout
# ==============================

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.signin"))