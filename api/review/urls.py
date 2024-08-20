from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReviewViewSet, ReviewGroupedByRateView

router = DefaultRouter()
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reviews/<int:product_id>/', ReviewGroupedByRateView.as_view(), name='reviews_grouped_by_rate'),
]
