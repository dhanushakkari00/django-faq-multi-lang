from django.test import TestCase
from faq.models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_faq_creation(self):
        """Test if FAQ is created correctly."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a high-level Python web framework.")

    def test_translation_fallback(self):
        """Test if translation fallback to English works."""
        self.assertEqual(self.faq.get_translation(lang="es"), "What is Django?")  # Assuming no Spanish translation
