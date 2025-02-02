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
git clone https://github.com/YOUR_GITHUB_USERNAME/faq_project.git
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

### 4. Configure Environment Variables
Create a `.env` file in the project root and add the required environment variables:

```ini
DJANGO_SECRET_KEY=your_secret_key_here
REDIS_URL=redis://127.0.0.1:6379/1
```

### 5. Apply Database Migrations
Run the following command to set up the database:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
If you want access to the Django Admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username and password.

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

#### Example Response
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "<p>Django is a web framework.</p>"
    }
]
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
- **Superuser credentials** (if created):
  ```
  Username: admin
  Password: admin123
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

To run tests while ignoring warnings:

```bash
pytest --disable-warnings
```

---

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

## Contributing

Contributions are welcome. Follow the steps below to contribute:

1. **Fork the repository** on GitHub.
2. **Clone your forked repository**:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/faq_project.git
   ```
3. **Create a new feature branch**:
   ```bash
   git checkout -b feature-new-update
   ```
4. **Make your changes and commit them**:
   ```bash
   git add .
   git commit -m "feat: Added new FAQ feature"
   ```
5. **Push changes to GitHub**:
   ```bash
   git push origin feature-new-update
   ```
6. **Create a pull request** on GitHub.

---

## Version Control and Commit Guidelines

Follow the **conventional commit message format** for clarity:

| Type     | Description |
|----------|------------|
| `feat:`  | A new feature |
| `fix:`   | A bug fix |
| `docs:`  | Documentation updates |
| `test:`  | Adding or updating tests |
| `chore:` | Maintenance tasks |

Examples:

```bash
git commit -m "feat: Add API support for multiple languages"
git commit -m "fix: Resolve translation caching issue"
git commit -m "docs: Update README with API examples"
```

---

## License

This project is licensed under the **MIT License**. You are free to modify and distribute it as needed.

---

## Acknowledgements

- Django REST Framework for API support.
- Google Translate API for multilingual translations.
- Redis for caching to enhance performance.
- Pytest for unit testing.

