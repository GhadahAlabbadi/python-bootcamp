from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='list'),
    path('category/<str:category>/', views.course_category, name='category'),
    path('<slug:slug>/', views.course_detail, name='detail'),
]