from celery import shared_task
import requests
from .models import ExchangeRateLog

@shared_task
def fetch_usd_to_bdt():
    res = requests.get("https://open.er-api.com/v6/latest/USD")
    data = res.json()
    rate = data['rates'].get('BDT')
    if rate:
        ExchangeRateLog.objects.create(
            base_currency='USD',
            target_currency='BDT',
            rate=rate
        )
