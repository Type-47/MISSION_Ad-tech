from django.shortcuts import render
from django.views.generic import ListView
from .models import User_Info

# Create your views here.
class User_Info_View(ListView):
        model = User_Info
        template_name = 'user_info_list.html'

