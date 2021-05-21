from django.contrib import admin
from django.urls import path
from .views import index, elements, generic, aula, web, edu, labs, lab01, lab02, lab03, lab04, lab05, lab06, lab07, lab08, book_list, upload

from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('elements/', elements),
    path('generic/', generic),
    path('aula/', aula),
    path('web/', web),
    path('edu/', edu),
    path('labs/', labs),
    path('lab01/', lab01),
    path('lab02/', lab02),
    path('lab03/', lab03),
    path('lab04/', lab04),
    path('lab05/', lab05),
    path('lab06/', lab06),
    path('lab07/', lab07),
    path('lab08/', lab08),
    path('book_list/', book_list),
    path('book_list/upload/', upload)
]