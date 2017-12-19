from rest_framework import generics, filters
from .serializers import MemoSerializer
from .models import Memos

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Memos.objects.all()
    serializer_class = MemoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Memo."""
        serializer.save()

class ListView(generics.ListAPIView):
    """This class defines the Listing behavior of our rest api."""
    queryset = Memos.objects.all()
    serializer_class = MemoSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('date', 'id')
    search_fields = ('date', 'person')