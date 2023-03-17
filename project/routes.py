from flask import Blueprint, render_template, redirect, url_for, flash
from project.forms import RegisterForm, LoginForm

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email_address.data == "jhonielvillacura04@gmail.com" and form.password.data == "potanginamo":
            flash(f"Welcome back sir", "success")
            return redirect(url_for('views.home'))
        else:
            flash(f"Wrong data sorry", "danger")

    return render_template("login.html", form=form)

@views.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): 
        flash(f"You can now logged in!", "success")
        return redirect(url_for('views.login'))
     
    return render_template("register.html", form=form)
