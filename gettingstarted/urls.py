from django.urls import path, include
import hello.views


urlpatterns = [path("", include("hello.urls"))]
