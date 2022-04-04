from rest_framework import serializers

from webapp.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('id', 'text', 'email', 'name', 'rating', 'status')
        read_only_fields = ('rating', 'status')
