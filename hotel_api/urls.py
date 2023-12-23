from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('guests', views.GuestViewSet, basename='guests')
router.register('cabins', views.CabinViewSet, basename='cabins')
router.register('settings', views.SettingViewSet, basename='settings')
router.register('bookings', views.BookingViewSet, basename='bookings')
router.register('todos', views.TodoViewSet)

urlpatterns = router.urls