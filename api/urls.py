from django.urls import path
from .views import User_InfoAPIView

urlpatterns = [
    path('',User_InfoAPIView.as_view()),
]
