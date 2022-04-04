
from rest_framework import viewsets

from api_v1.seraillizers import QuoteSerializer
from webapp.models import Quote


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

