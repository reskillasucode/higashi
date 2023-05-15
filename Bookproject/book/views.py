from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from .models import Book

# Create your views here.

class BookList(ListView):
    template_name = 'list.html'
    model = Book

class BookListAPI(APIView):
    permission_classes = []