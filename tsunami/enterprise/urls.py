from django.contrib import admin
from django.urls import path
from enterprise.views.category.views import *

app_name = 'enterprise'

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]
