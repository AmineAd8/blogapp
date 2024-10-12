from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='blog-index'),
    path('comment/<int:pk>/', views.comment, name='blog-comment'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),

]