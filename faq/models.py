from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    # Main Question and Answer
    question = models.TextField()
    answer = RichTextField()

    # Translated Questions
    question_hi = models.TextField(null=True, blank=True)  # Hindi
    question_bn = models.TextField(null=True, blank=True)  # Bengali
    question_ta = models.TextField(null=True, blank=True)  # Tamil
    question_te = models.TextField(null=True, blank=True)  # Telugu
    question_mr = models.TextField(null=True, blank=True)  # Marathi
    question_ml = models.TextField(null=True, blank=True)  # Malayalam
    question_kn = models.TextField(null=True, blank=True)  # Kannada

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translation(self, lang='en'):
        """
        Returns the question in the specified language.
        Falls back to English if the translation is unavailable.
        """
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
            'ta': self.question_ta,
            'te': self.question_te,
            'mr': self.question_mr,
            'ml': self.question_ml,
            'kn': self.question_kn,
        }
        return translations.get(lang, self.question) or self.question

    def __str__(self):
        return self.question[:50]  # Show first 50 characters of the question
