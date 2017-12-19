from rest_framework import generics, filters
from .serializers import MemoSerializer
from .models import Memos

class AddView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = MemoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Memo."""
        serializer.save()

class HistoryView(generics.ListAPIView):
    """This class defines the Listing behavior of our rest api."""
    queryset = Memos.objects.all()
    serializer_class = MemoSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('date', 'id')
    search_fields = ('date', 'person')