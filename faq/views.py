from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    """
    API view to list all FAQs with language support.
    """
    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')  # Default to English
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
        return Response(serializer.data, status=status.HTTP_200_OK)
