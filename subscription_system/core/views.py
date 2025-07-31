from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from datetime import timedelta, date
import requests
from .models import Plan, Subscription, ExchangeRateLog
from .serializers import SubscriptionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from django.contrib.auth.models import User

class SubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @transaction.atomic
    def post(self, request):
        plan_id = request.data.get('plan_id')
        plan = Plan.objects.get(id=plan_id)
        end_date = date.today() + timedelta(days=plan.duration_days)
        subscription = Subscription.objects.create(
            user=request.user,
            plan=plan,
            end_date=end_date,
            status='active'
        )
        return Response({'message': 'Subscribed successfully'}, status=201)

class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

class CancelSubscriptionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        sub_id = request.data.get('subscription_id')
        subscription = Subscription.objects.get(id=sub_id, user=request.user)
        subscription.status = 'cancelled'
        subscription.save()
        return Response({'message': 'Subscription cancelled'}, status=200)

class ExchangeRateView(APIView):
    def get(self, request):
        base = request.GET.get('base')
        target = request.GET.get('target')
        url = f"https://open.er-api.com/v6/latest/{base}"
        res = requests.get(url)
        data = res.json()

        if target in data['rates']:
            rate = data['rates'][target]
            ExchangeRateLog.objects.create(
                base_currency=base,
                target_currency=target,
                rate=rate
            )
            return Response({'rate': rate}, status=200)
        return Response({'error': 'Invalid currency'}, status=400)


def subscription_table(request):
    users = User.objects.all()
    return render(request, 'core/subscriptions.html', {'users': users})