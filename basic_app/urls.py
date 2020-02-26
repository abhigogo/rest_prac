from django.conf.urls import url, include
from rest_framework import routers
from basic_app import views

router = routers.DefaultRouter()
router.register('languages',views.LanguageView)

urlpatterns = [
    url(r'',include(router.urls))
]