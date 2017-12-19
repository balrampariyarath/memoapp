from rest_framework import serializers
from .models import Memos


class MemoSerializer(serializers.ModelSerializer):
    """Serializer to map model Instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Memos
        fields = ('id', 'desc', 'image', 'date', 'person')