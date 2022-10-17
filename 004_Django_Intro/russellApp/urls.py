from django.urls import path

from .views import russell
# from fscohortApp.views import fshome
urlpatterns = [
    path('',russell),
]
