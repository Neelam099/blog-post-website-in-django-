from django.urls import path
from .import views


app_name = "myprofile"

urlpatterns = [
    path("create_account", views.register_user, name="create"),
    path("signin", views.login_user, name="signin"),
    path("logout", views.signout, name = "signout"),
    path("update_profile", views.update_profile, name="update_profile"),
    path('user_profile', views.user_profile, name = "profile")
]
