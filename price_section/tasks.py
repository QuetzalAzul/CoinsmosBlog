from time import sleep
from celery import task
from celery import Celery
from .models import Crypto
import requests
import certifi
import re

@task()
def crawl_currency():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false&price_change_percentage='24h'"

    response = requests.get(url,verify=certifi.where())
    transaction_content = response.json()

    for crypto_content in transaction_content:
        Crypto.objects.create(
        cryptocurrency = crypto_content["name"],
        precio = crypto_content["current_price"],
        marketcap = crypto_content["market_cap"],
        volumen = crypto_content["total_volume"],
        supply = crypto_content["circulating_supply"],
        change = crypto_content["price_change_percentage_24h"],
        imagen = crypto_content["image"]
        )

        sleep(3)

@task()
def update_currency():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false&price_change_percentage='24h'"
    response = requests.get(url,verify=certifi.where())
    transaction_content = response.json()
    i = 0
    pattern = re.compile(r'.*(?=\.)')
    pattern2 = re.compile(r'(.*)\.\d\d')
    for crypto_content in transaction_content:
        crypto = Crypto.objects.all()[i]
        crypto.cryptocurrency = crypto_content["name"]
        crypto.precio = crypto_content["current_price"]
        crypto.marketcap = crypto_content["market_cap"]
        crypto.volumen = crypto_content["total_volume"]
        supply = crypto_content["circulating_supply"]
        change = crypto_content["price_change_percentage_24h"]
        match = pattern.match(str(supply))
        match2 = pattern2.match(str(change))
        if match:
            crypto.supply = match[0]
            crypto.change = match2[0]
        crypto.imagen = crypto_content["image"]
        crypto.save(update_fields=['cryptocurrency','precio','marketcap','volumen','supply', 'change', 'imagen'])
        i += 1

if not Crypto.objects.all():
    crawl_currency()

while True:
    sleep(3600)
    update_currency()
