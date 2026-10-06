# Books App

Flask CRUD project for managing books.

## Project structure

```text
/books-app
    /templates
        create_book.html
    /migrations
        /versions
    app.py
    config.py
    requirements.txt
    README.md
```

## 1. Create the MySQL database

Open MySQL and run:

```sql
CREATE DATABASE lesson35_hw;
```

The `books` table is created through Flask-Migrate.

## 2. Configure database connection

Open `config.py` and change:

```python
mysql+pymysql://root:password@localhost/lesson35_hw
```

For example, if your MySQL root user has no password:

```python
mysql+pymysql://root:@localhost/lesson35_hw
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Initialize migrations

If the included migration folder is not yet initialized in your environment:

```bash
flask --app app db init
```

Then create a migration:

```bash
flask --app app db migrate -m "create books table"
```

Apply it:

```bash
flask --app app db upgrade
```

Alternatively, the included `migrations/versions` directory contains a migration file that creates the `books` table.

## 5. Run the application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## Endpoints

### Add book

```text
GET  /book
POST /book
```

Open `/book` in the browser to see the HTML form.

### Update book

```text
GET  /update_book/<book_id>
POST /update_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/update_book/1
```

### Get one book

```text
GET /get_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/get_book/1
```

### Get all books

```text
GET /books
```

### Delete book

```text
DELETE /delete_book/<book_id>
```

Example with curl:

```bash
curl -X DELETE http://127.0.0.1:5000/delete_book/1
```

## Database table

The `books` table contains:

| Field | Type |
|---|---|
| id | Integer, Primary Key |
| title | String |
| author | String |
| year | Integer |
