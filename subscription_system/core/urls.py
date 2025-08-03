from django.urls import path
from .views import SubscribeView, SubscriptionListView, CancelSubscriptionView, ExchangeRateView, subscription_table
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribe/', SubscribeView.as_view()),
    path('subscriptions/', SubscriptionListView.as_view()),
    path('cancel/', CancelSubscriptionView.as_view()),
    path('exchange-rate/', ExchangeRateView.as_view()),
    path('subscription/', subscription_table),
]
