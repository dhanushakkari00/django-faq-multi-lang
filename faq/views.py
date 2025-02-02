from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()
        faq_list = []

        for faq in faqs:
            translated_question, translated_answer = faq.get_translation(lang)
            faq_list.append({
                "id": faq.id,
                "question": translated_question,
                "answer": translated_answer,
                "created_at": faq.created_at,
                "updated_at": faq.updated_at
            })

        return Response(faq_list)