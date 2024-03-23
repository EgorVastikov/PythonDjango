from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poem/', views.create_record, name='create_record'),
    path('add_note/', views.add_note, name='add_note'),
]