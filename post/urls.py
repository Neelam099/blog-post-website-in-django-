from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    
    path("", views.index, name='index'),
    path("article/<str:slug>", views.detail, name='detail'),
    path("create_post", views.create_post, name = "create"),
    path("update_post/<str:slug>", views.update_post, name = "update"),
    path("delete_post/<str:slug>", views.delete_post, name = "delete"),
    
]