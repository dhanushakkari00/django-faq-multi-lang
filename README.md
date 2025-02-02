# Django Multilingual FAQ Web Application

This is a Django-based FAQ management web application that supports **WYSIWYG editor** and **multi-language translations**. It provides a **REST API** for retrieving FAQs dynamically with caching for better performance.

---

## Features
- WYSIWYG Editor (`django-ckeditor`) for rich text formatting.
- Multi-language translation using `googletrans` with automatic fallback to English.
- Redis caching for improved API response time.
- REST API with `?lang=` query parameter for language selection.
- Django Admin panel for managing FAQs.
- Unit tests implemented using `pytest`.

---

## Installation Guide

### 1. Clone the Repository
To set up the project locally, first, clone the repository:

```bash
git clone https://github.com/dhanushakkari00/faq_project.git
cd faq_project
```

### 2. Create and Activate a Virtual Environment
Creating a virtual environment ensures dependencies are installed in an isolated environment.

```bash
python -m venv envi
```

For **Windows**:
```bash
envi\Scripts\activate
```

For **Mac/Linux**:
```bash
source envi/bin/activate
```

### 3. Install Required Dependencies
All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```


### 4. Apply Database Migrations
Run the following command to set up the database:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
If you want access to the Django Admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```


### 7. Start the Django Development Server
Run the following command to start the server:

```bash
python manage.py runserver
```

The application will be accessible at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

This project provides a REST API for retrieving FAQs.

### 1. Get All FAQs with Language Support
```
GET /api/faqs/?lang=<language_code>
```

#### Example Request
```bash
curl "http://127.0.0.1:8000/api/faqs/?lang=hi"
```



Supported languages:
- `hi` - Hindi
- `bn` - Bengali
- `ta` - Tamil
- `te` - Telugu
- `mr` - Marathi
- `ml` - Malayalam
- `kn` - Kannada
- Default is English (`en`)

---

## Admin Panel

The Django Admin panel provides a user-friendly interface for managing FAQs.

- **URL:** `http://127.0.0.1:8000/admin/`
- **Superuser credentials** :
  ```
  Username: dhanushakkari
  Password: bharathfd
  ```

To access the panel, create a superuser if you haven't already:

```bash
python manage.py createsuperuser
```

---

## Running Tests

This project includes unit tests to validate API functionality and model behavior.

### Run All Tests
To run the test suite:

```bash
pytest
```



## Project Structure

Below is an overview of the project's directory structure:

```
faq_project/
│── faq/                      # Main Django app
│   ├── migrations/           # Database migrations
│   ├── tests/                # Unit tests
│   ├── views.py              # API Views
│   ├── models.py             # Database Models
│   ├── serializers.py        # API Serializers
│   ├── urls.py               # API URL Routes
│── faq_project/              # Django project settings
│── static/                   # Static files
│── templates/                # HTML Templates
│── manage.py                 # Django Management Script
│── requirements.txt          # Python dependencies
│── README.md                 # Project Documentation
```

---



## Acknowledgements

- Django REST Framework for API support.
- Google Translate API for multilingual translations.
- Redis for caching to enhance performance.
- Pytest for unit testing.

