from django.urls import path
from .views import HomeView, XabarView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("xabarlar/", XabarView.as_view(), name="xabarlar"),
]
