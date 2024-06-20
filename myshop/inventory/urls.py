from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ConsoleViewSet, AccessoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'consoles', ConsoleViewSet)
router.register(r'accessories', AccessoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
