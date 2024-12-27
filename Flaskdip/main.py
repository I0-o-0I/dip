from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articlesmanager.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/articles')
def article_all():
    if request.args.get('q'):
        articles = Article.query.filter(request.args.get('q') == Article.title)
    else:
        articles = Article.query.order_by(Article.title).all()
    return render_template('all_articles.html', articles=articles)


@app.route('/create', methods=['POST', 'GET'])
def article_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        article= Article(title=title, content=content)
        db.session.add(article)
        db.session.commit()
        return redirect('/articles')
    else:
        return render_template('create.html')

@app.route('/articles/<int:id>')
def article_one(id):
    article = Article.query.get_or_404(id)
    return render_template('article_one.html', article=article)

@app.route('/articles/<int:id>/update', methods=['POST', 'GET'])
def article_update(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        db.session.commit()
        return redirect('/articles')
    else:
        return render_template('update.html', article=article)

@app.route('/articles/<int:id>/delete_question')
def question(id):
    article = Article.query.get_or_404(id)
    return render_template('question.html', article=article)

@app.route('/articles/<int:id>/delete')
def article_delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect('/articles')




if __name__ == '__main__':
    app.run(debug=False)
