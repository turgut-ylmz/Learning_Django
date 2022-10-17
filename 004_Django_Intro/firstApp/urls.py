from django.urls import path

from .views import home
# from fscohortApp.views import fshome
urlpatterns = [
    path('',home),
]
