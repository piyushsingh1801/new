from django.urls import path
from .views import SongsView
urlpatterns = [
    path('media/',SongsView.as_view()),
    path('media/<int:id>',SongsView.as_view())
]
