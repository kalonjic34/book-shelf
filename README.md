# Book Shelf

A Django-based book management web application for organising and working with a personal collection of books.

## Features

* User account functionality
* Book library management
* Add and manage books
* Browse books in the library
* Django-based application structure
* Database-backed book management

## Built With

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **JavaScript**
* **Django Templates**
* **Django ORM**
* **Django Authentication**

## Project Structure

```text
book-shelf/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── book_library/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── bookshelf/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── .gitignore
```

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.10+
* pip
* Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/kalonjic34/book-shelf.git
```

2. Navigate into the project:

```bash
cd book-shelf
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment.

**Windows:**

```powershell
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

5. Install the project dependencies:

```bash
pip install django
```

6. Apply the database migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Application Structure

### Accounts

The `accounts` app handles functionality related to users and account management.

### Book Library

The `book_library` app contains the main book management functionality and handles the application's library-related data and views.

### Bookshelf

The `bookshelf` directory contains the main Django project configuration, including settings, URL routing, and WSGI/ASGI configuration.

## Django Implementation

The application uses Django's core functionality for:

* Django project and app structure
* URL routing
* Views
* Django templates
* Models and migrations
* Django ORM
* Database relationships
* User accounts
* Form handling
* Django admin

## Running the Development Server

After activating the virtual environment:

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

To stop the server, press `CTRL + C`.

## Future Improvements

Potential improvements for the application include:

* Book search and filtering
* Book categories or genres
* Book cover uploads
* Reading status tracking
* Personal reading lists
* Book ratings and reviews
* Pagination for larger libraries
* REST API integration
* Improved user profiles

## Purpose

Book Shelf was built to develop my understanding of building database-driven web applications with Python and Django through a practical application.

The project focuses on applying Django to user accounts and book management while working with models, views, templates, forms, database operations, and application structure.

## License

This project is for portfolio and personal development purposes.
