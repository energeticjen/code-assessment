from django.urls import path
from . import views

app_name = "signup"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("submit/", views.SubmitView.as_view(), name="submit"),
    path("confirm/", views.ConfirmView.as_view(), name="confirm"),
]