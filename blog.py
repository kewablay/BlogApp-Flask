from email.policy import default
from unicodedata import category
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f"{self.title}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.author}')"



@app.route('/')
def home():
    all_post = Post.query.all()
    categories = Category.query.all()
    return render_template('index.html', posts=all_post, categories=categories)

@app.route('/new-post',methods=['GET', 'POST'])
def newPost():
    return render_template('new-post.html')

if __name__ == "__main__":
    app.run(debug=True)