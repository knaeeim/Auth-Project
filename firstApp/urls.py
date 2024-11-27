from django.urls import path, include
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", user_logout, name="logout"),
    path("pass_change/", pass_change, name="passchange"),
    path("set_pass/", pass_set, name="pass_set"),
    path("edit_profile/", editProfileData, name="editProfile"),
]