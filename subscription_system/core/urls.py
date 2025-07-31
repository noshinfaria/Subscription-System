from django.urls import path
from .views import SubscribeView, SubscriptionListView, CancelSubscriptionView, ExchangeRateView, subscription_table

urlpatterns = [
    path('subscribe/', SubscribeView.as_view()),
    path('subscriptions/', SubscriptionListView.as_view()),
    path('cancel/', CancelSubscriptionView.as_view()),
    path('exchange-rate/', ExchangeRateView.as_view()),
    path('subscription/', subscription_table),
]
