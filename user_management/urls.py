from django.urls import path

from .views import User_Info_View


urlpatterns = [
    path('', User_Info_View.as_view(), name='home')
]
