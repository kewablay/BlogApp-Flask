from unicodedata import category
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey())


@app.route('/')
def blog():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)