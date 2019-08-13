from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

@app.route('/') # ルート(/)ページURLにリクエストが送られた時の処理
def index():

    posts = Post.query.all()
    return render_template("index.html", posts = posts)