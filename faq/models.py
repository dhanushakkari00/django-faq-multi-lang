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

    # Translated Answers
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)
    answer_ta = RichTextField(null=True, blank=True)
    answer_te = RichTextField(null=True, blank=True)
    answer_mr = RichTextField(null=True, blank=True)
    answer_ml = RichTextField(null=True, blank=True)
    answer_kn = RichTextField(null=True, blank=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Automatically translate the `question` and `answer` into multiple languages
        before saving the object.
        """
        translator = Translator()

        if not self.pk or not all([self.question_hi, self.answer_hi]):
            try:
                # Translate Questions
                self.question_hi = self.question_hi or translator.translate(self.question, src='en', dest='hi').text
                self.question_bn = self.question_bn or translator.translate(self.question, src='en', dest='bn').text
                self.question_ta = self.question_ta or translator.translate(self.question, src='en', dest='ta').text
                self.question_te = self.question_te or translator.translate(self.question, src='en', dest='te').text
                self.question_mr = self.question_mr or translator.translate(self.question, src='en', dest='mr').text
                self.question_ml = self.question_ml or translator.translate(self.question, src='en', dest='ml').text
                self.question_kn = self.question_kn or translator.translate(self.question, src='en', dest='kn').text

                # Translate Answers
                self.answer_hi = self.answer_hi or translator.translate(self.answer, src='en', dest='hi').text
                self.answer_bn = self.answer_bn or translator.translate(self.answer, src='en', dest='bn').text
                self.answer_ta = self.answer_ta or translator.translate(self.answer, src='en', dest='ta').text
                self.answer_te = self.answer_te or translator.translate(self.answer, src='en', dest='te').text
                self.answer_mr = self.answer_mr or translator.translate(self.answer, src='en', dest='mr').text
                self.answer_ml = self.answer_ml or translator.translate(self.answer, src='en', dest='ml').text
                self.answer_kn = self.answer_kn or translator.translate(self.answer, src='en', dest='kn').text

            except Exception as e:
                print(f"Translation failed: {e}")

        super().save(*args, **kwargs)  # Call the parent save method

    def get_translation(self, lang='en'):
        """
        Returns the translated question and answer for the given language.
        Uses Redis caching to improve performance.
        """
        cache_key = f"faq_translation_{self.id}_{lang}"  # Unique cache key
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation  # Return cached version

        # Fetch stored translations
        translations = {
            'hi': (self.question_hi, self.answer_hi),
            'bn': (self.question_bn, self.answer_bn),
            'ta': (self.question_ta, self.answer_ta),
            'te': (self.question_te, self.answer_te),
            'mr': (self.question_mr, self.answer_mr),
            'ml': (self.question_ml, self.answer_ml),
            'kn': (self.question_kn, self.answer_kn),
        }

        translated_question, translated_answer = translations.get(lang, (self.question, self.answer))

        # Store in cache (expires in 24 hours)
        cache.set(cache_key, (translated_question, translated_answer), timeout=86400)

        return translated_question or self.question, translated_answer or self.answer

    def __str__(self):
        return self.question[:50]  # Show first 50 characters of the question
