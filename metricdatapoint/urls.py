from termios import VREPRINT
from django.urls import path

from rest_framework.routers import SimpleRouter
from user import views

from metricdatapoint import views

router = SimpleRouter()
router.register('', views.DataViewSet)


urlpatterns=[
]+ router.get_urls()