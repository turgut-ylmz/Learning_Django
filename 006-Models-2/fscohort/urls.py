from django.urls import path

from .views import fscohort, subfolder
urlpatterns = [
    path('', fscohort), # /fschohort/
    path('subfolder/', subfolder), # /fschohort/subfolder/
]
