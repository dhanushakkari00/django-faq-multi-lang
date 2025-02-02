# Use official Python image
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=faq_project.settings
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_project.wsgi:application"]
