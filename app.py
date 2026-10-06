from flask import Flask, render_template, request, redirect, url_for, jsonify
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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }


@app.route("/book", methods=["GET", "POST"])
def create_book():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        year = request.form.get("year", "").strip()

        if not title or not author or not year:
            return "ყველა ველის შევსება სავალდებულოა.", 400

        try:
            year = int(year)
        except ValueError:
            return "წელი უნდა იყოს რიცხვი.", 400

        book = Book(title=title, author=author, year=year)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("get_books"))

    return render_template("create_book.html")


@app.route("/update_book/<int:book_id>", methods=["GET", "POST"])
def update_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        year = request.form.get("year", "").strip()

        if not title or not author or not year:
            return "ყველა ველის შევსება სავალდებულოა.", 400

        try:
            year = int(year)
        except ValueError:
            return "წელი უნდა იყოს რიცხვი.", 400

        book.title = title
        book.author = author
        book.year = year

        db.session.commit()
        return redirect(url_for("get_book", book_id=book.id))

    return f"""
    <h1>Update Book</h1>
    <form method="POST">
        <label>Title:</label><br>
        <input type="text" name="title" value="{book.title}" required><br><br>

        <label>Author:</label><br>
        <input type="text" name="author" value="{book.author}" required><br><br>

        <label>Year:</label><br>
        <input type="number" name="year" value="{book.year}" required><br><br>

        <button type="submit">Update</button>
    </form>
    """


@app.route("/get_book/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book.to_dict())


@app.route("/books", methods=["GET"])
def get_books():
    books = db.session.scalars(
        db.select(Book).order_by(Book.id)
    ).all()

    return jsonify([book.to_dict() for book in books])


@app.route("/delete_book/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Book deleted successfully",
        "book": book.to_dict()
    })


if __name__ == "__main__":
    app.run(debug=True)
