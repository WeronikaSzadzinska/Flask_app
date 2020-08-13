from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/mypage/me", methods = ["GET"])
def home():
    return render_template("homepage.html")

@app.route("/mypage/contact", methods = ["GET"])
def contact():
    return render_template("contact.html")


@app.route("/mypage/message", methods = ["POST", "GET"])
def message():
    return render_template("message.html")