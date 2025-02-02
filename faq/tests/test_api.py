import pytest
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    FAQ.objects.create(question="What is Redis?", answer="Redis is a caching system.")
    
    response = client.get("/api/faqs/?lang=en")
    
    assert response.status_code == 200
    assert response.data[0]["question"] == "What is Redis?"
