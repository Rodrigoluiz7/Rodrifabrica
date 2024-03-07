from rest_framework.routers import DefaultRouter
from.viewsets import 
from django.urls import include,path
router =  DefaultRouter()


router.register("pessoa",PesooaViewSet)

urlpatterns = [
    path("api",include(router.urls))
]