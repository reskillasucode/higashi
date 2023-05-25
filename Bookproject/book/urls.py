from django.contrib import admin
from django.urls import path
from .views import BookList, BookListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', BookList.as_view()),
    path('api/', BookListAPI.as_view()),
]
