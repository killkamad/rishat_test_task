import random

from django.shortcuts import render
from django.http import JsonResponse
import stripe
from core.models import Item
from django.conf import settings


def get_checkout_session(request, item_id):
    stripe.api_key = settings.STRIPE_API_KEY
    item = Item.objects.get(id=item_id)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'unit_amount': int(item.price * 100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://localhost:8000/success/{item_id}',
        cancel_url=f'http://localhost:8000/cancel/{item_id}',
    )
    return JsonResponse({'session_id': checkout_session.id})


def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    public_key = settings.STRIPE_PUBLIC_KEY
    return render(request, 'item_detail.html', {'item': item, 'public_key': public_key})


def success_page_view(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'success.html', {'item': item})


def cancel_page_view(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'cancel.html', {'item': item})
