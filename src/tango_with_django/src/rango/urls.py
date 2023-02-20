from django.urls import path
from . import views

app_name = 'rango'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='category'),
    path('', views.index, name='index'),
]
