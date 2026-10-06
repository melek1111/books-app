from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    books = db.session.scalars(
        db.select(Book).order_by(Book.id)
    ).all()

    return render_template("books.html", books=books)


@app.route("/book", methods=["GET", "POST"])
def create_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = int(request.form["year"])

        book = Book(
            title=title,
            author=author,
            year=year
        )

        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books"))

    return render_template("create_book.html")


@app.route("/update_book/<int:book_id>", methods=["GET", "POST"])
def update_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return "Book not found", 404

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.year = int(request.form["year"])

        db.session.commit()

        return redirect(url_for("books"))

    return render_template("update_book.html", book=book)


@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return "Book not found", 404

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("books"))


@app.route("/get_book/<int:book_id>")
def get_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return "Book not found", 404

    return render_template("get_book.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)