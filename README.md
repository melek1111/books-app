# Books App

Flask CRUD project for managing books.

## Project Structure

```text
/books-app
├── templates/
│   └── create_book.html
├── migrations/
│   └── versions/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## 1. Create the MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE lesson35_hw;
```

The `books` table is created through Flask-Migrate.

## 2. Configure Database Connection

Create a `.env` file in the project root:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/lesson35_hw
```

Replace `YOUR_PASSWORD` with your MySQL root password.

The `.env` file is excluded from Git using `.gitignore`.

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Apply Database Migration

Apply the existing migration:

```bash
flask db upgrade
```

To check whether the database schema is up to date:

```bash
flask db check
```

If the SQLAlchemy models are changed, create a new migration:

```bash
flask db migrate -m "description of changes"
```

Then apply it:

```bash
flask db upgrade
```

## 5. Run the Application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## Endpoints

### Add Book

```text
GET  /book
POST /book
```

Open `/book` in the browser to see the HTML form.

### Update Book

```text
GET  /update_book/<book_id>
POST /update_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/update_book/1
```

### Get One Book

```text
GET /get_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/get_book/1
```

### Get All Books

```text
GET /books
```

Example:

```text
http://127.0.0.1:5000/books
```

### Delete Book

```text
DELETE /delete_book/<book_id>
```

Example with PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/delete_book/1" -Method DELETE
```

## Database Table

The `books` table contains:

| Field  | Type                 |
| ------ | -------------------- |
| id     | Integer, Primary Key |
| title  | String               |
| author | String               |
| year   | Integer              |
