from django.urls import path
from . import views


app_name = "polls"
urlpatterns= [
    path("", views.IndexView.as_view(), name="index"),
    path("registration/", views.registration, name="registration"),
    path("register/", views.register, name="register"),
    path("login/", views.loginForm, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("authenticateUser", views.authenticateUser, name="authenticateUser"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]