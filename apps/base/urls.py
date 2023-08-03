from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.HomepageView.as_view(), name="home_page"),
    path("about/", views.AboutUsView.as_view(), name="about"),
]
