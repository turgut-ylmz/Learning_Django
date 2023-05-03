from rest_framework import routers
from .views import FlightView, ReservationView


router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('resv', ReservationView)

urlpatterns = [
    
]

urlpatterns += router.urls


