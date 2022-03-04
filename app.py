from email.policy import default
from unicodedata import category
from datetime import datetime
from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
server = app.server


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f"{self.title}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content_link = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_posted = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.id}')"



@app.route('/')
def home():
    all_post = Post.query.all()
    categories = Category.query.all()
    return render_template('index.html', posts=all_post, categories=categories)


@app.route('/<int:id>', methods=['GET', 'POST'])
def postDetail(id):
    post = Post.query.get(id)
    return render_template("detail.html", post=post)


@app.route('/new-post',methods=['GET', 'POST'])
def newPost():
    if request.method == "POST":
        category_id = int(request.form['categoriesOption'])
        title = request.form['title']
        content = request.form['content']
        date_posted = datetime.utcnow
        
        new_post = Post(category_id=category_id, title=title, content=content, date_posted = date_posted)
    
        db.session.add(new_post)
        db.session.commit()
        
        print("post created successfully...")
        
        return redirect('/')
    
    return render_template('new-post.html')

if __name__ == "__main__":
    app.run(debug=True)