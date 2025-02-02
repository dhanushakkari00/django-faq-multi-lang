from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache



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

    def save(self, *args, **kwargs):
        """
        Automatically translate the `question` into multiple languages
        and store them in respective fields before saving the object.
        """
        translator = Translator()
        if not self.pk or not all([self.question_hi, self.question_bn, self.question_ta]):
            # Only translate if creating a new object or missing translations
            try:
                self.question_hi = self.question_hi or translator.translate(self.question, src='en', dest='hi').text
                self.question_bn = self.question_bn or translator.translate(self.question, src='en', dest='bn').text
                self.question_ta = self.question_ta or translator.translate(self.question, src='en', dest='ta').text
                self.question_te = self.question_te or translator.translate(self.question, src='en', dest='te').text
                self.question_mr = self.question_mr or translator.translate(self.question, src='en', dest='mr').text
                self.question_ml = self.question_ml or translator.translate(self.question, src='en', dest='ml').text
                self.question_kn = self.question_kn or translator.translate(self.question, src='en', dest='kn').text
            except Exception as e:
                print(f"Translation failed: {e}")

        super().save(*args, **kwargs)  # Call the parent save method

    def get_translation(self, lang='en'):
        """
        Returns the translated question for the given language.
        Uses Redis caching to improve performance.
        """
        cache_key = f"faq_translation_{self.id}_{lang}"  # Unique cache key
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation  # Return cached version

        # If not cached, translate dynamically
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
            'ta': self.question_ta,
            'te': self.question_te,
            'mr': self.question_mr,
            'ml': self.question_ml,
            'kn': self.question_kn,
        }

        translation = translations.get(lang, self.question) or self.question

        # Store in cache for future requests (expires in 24 hours)
        cache.set(cache_key, translation, timeout=86400)

        return translation
    def __str__(self):
        return self.question[:50]  # Show the first 50 characters of the question
