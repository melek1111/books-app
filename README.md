# Books App

Flask CRUD project for managing books.

## Project Structure

```text
/books-app
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── create_book.html
│   ├── update_book.html
│   └── get_book.html
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

The form allows the user to enter:

- Book title
- Author
- Publication year

After submitting the form, the book is saved to the database and the user is redirected to the books list.

### Update Book

```text
GET  /update_book/<book_id>
POST /update_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/update_book/1
```

The existing book information is displayed in an HTML form.

After submitting the form, the selected book is updated in the database.

### Get One Book

```text
GET /get_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/get_book/1
```

This endpoint displays information about one specific book.

The displayed information includes:

- ID
- Title
- Author
- Year

### Get All Books

```text
GET /books
```

Example:

```text
http://127.0.0.1:5000/books
```

This endpoint displays all books stored in the database.

The books are displayed in a table with the following information:

- ID
- Title
- Author
- Year

Each book also has the following actions:

- Edit
- Delete
- Get Book

### Delete Book

```text
GET /delete_book/<book_id>
```

Example:

```text
http://127.0.0.1:5000/delete_book/1
```

This endpoint deletes the selected book from the database.

After deletion, the user is redirected to the books list.

## Database Table

The `books` table contains:

| Field  | Type                 |
| ------ | -------------------- |
| id     | Integer, Primary Key |
| title  | String               |
| author | String               |
| year   | Integer              |

## CRUD Operations

The application supports the following CRUD operations:

| Operation | Description               |
| --------- | ------------------------- |
| Create    | Add a new book            |
| Read      | Get one book or all books |
| Update    | Edit an existing book     |
| Delete    | Delete an existing book   |

## Application Pages

The application contains the following HTML pages:

### `base.html`

Contains the common layout and navigation used by the other pages.

The navigation provides links to:

- Home
- Books
- Add Book

### `index.html`

The home page of the application.

It provides links to:

- View Books
- Add New Book

### `books.html`

Displays all books stored in the database.

It also provides actions for each book:

- Edit
- Delete
- Get Book

### `create_book.html`

Contains the form used to create a new book.

The form contains:

- Title
- Author
- Year

### `update_book.html`

Contains the form used to update an existing book.

The current book information is automatically displayed in the form.

### `get_book.html`

Displays the details of a selected book.

## Database Configuration

The application uses environment variables for the database connection.

The database URL is stored in `.env`:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/lesson35_hw
```

The `.env` file should not be committed to GitHub because it contains database credentials.

The `.gitignore` file contains:

```text
.venv/
__pycache__/
*.pyc
.env
.vscode/
```

## Technologies Used

The project uses:

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- MySQL
- PyMySQL
- python-dotenv
- HTML
- Jinja2

## Flask-Migrate

Flask-Migrate is used to manage database schema changes.

The migration commands are:

```bash
flask db upgrade
```

To check the database schema:

```bash
flask db check
```

To create a new migration after changing the SQLAlchemy model:

```bash
flask db migrate -m "description of changes"
```

Then apply the migration:

```bash
flask db upgrade
```

## Running the Project

After installing the dependencies and configuring the database, run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The application can then be used through the browser.

## Project Flow

The basic flow of the application is:

```text
Browser
   ↓
Flask Route
   ↓
SQLAlchemy
   ↓
MySQL Database
```

For example, when adding a book:

```text
User opens /book
       ↓
HTML form is displayed
       ↓
User enters book information
       ↓
POST /book
       ↓
Flask receives the data
       ↓
SQLAlchemy creates a Book object
       ↓
Book is saved to MySQL
       ↓
User is redirected to /books
```
