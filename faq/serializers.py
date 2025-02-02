from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']

    def get_question(self, obj):
        """
        Return the question in the selected language or default to English.
        """
        lang = self.context.get('lang', 'en')
        translations = {
            'hi': obj.question_hi,
            'bn': obj.question_bn,
            'ta': obj.question_ta,
            'te': obj.question_te,
            'mr': obj.question_mr,
            'ml': obj.question_ml,
            'kn': obj.question_kn,
        }
        return translations.get(lang, obj.question) or obj.question

    def get_answer(self, obj):
        """
        Return the answer (currently the same for all languages).
        """
        return obj.answer
