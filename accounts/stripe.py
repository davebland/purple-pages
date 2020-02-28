from django.http import JsonResponse, HttpResponseBadRequest

import os
import stripe

# Setup api
stripe.api_key = os.getenv('STRIPE_SECRET_KEY','')

def stripe_payment_intent(payment_amount: int):
    try:
        payment_intent = stripe.PaymentIntent.create(amount=payment_amount, currency='gbp')
        return JsonResponse({'stripePublicKey': os.getenv('STRIPE_PUBLIC_KEY',''), 'stripeClientSecret': payment_intent.client_secret})
    except:        
        return HttpResponseBadRequest()