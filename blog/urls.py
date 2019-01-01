from django.urls import path

from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.post_add, name='post_add'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/edit', views.post_edit, name='post_edit'),
]
