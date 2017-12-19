from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns
from .views import AddView
from .views import HistoryView

urlpatterns = {
    url(r'^memos/add/', AddView.as_view(), name="create"),
    url(r'^memos/history/', HistoryView.as_view(), name="list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)