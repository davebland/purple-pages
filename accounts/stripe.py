from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

import os
import stripe
import json

from .models import Payment
from accounts.models import PPUser

# Setup api
stripe.api_key = os.getenv('STRIPE_SECRET_KEY','')

def stripe_payment_intent(subscription_details: dict):
    """ Create a payment intent and return as JSON """
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=subscription_details['payment_amount'], 
            currency='gbp',
            metadata={
                'period':subscription_details['period'],
                'ppuser':subscription_details['pp_username']
            }
        )
        return JsonResponse({
            'stripePublicKey': os.getenv('STRIPE_PUBLIC_KEY',''),
            'stripeClientSecret': payment_intent.client_secret,
            'subscriptionPeriod': subscription_details['period'],
            'paymentAmount': subscription_details['payment_amount']
        })
    except:
        # Create payment failed, return no detail for security        
        return HttpResponseBadRequest()

def stripe_confirm_payment(payment_confirmation_data):
    """ Handle successfull payment intent from Stripe """
    try:
        # Parse the POST data into JSON
        stripe_paymentintent_success = stripe.Event.construct_from(
            json.loads(payment_confirmation_data), stripe.api_key
        )        
        # Create a payment object with stripe data and save
        ppuser = PPUser.objects.get(username=stripe_paymentintent_success.data.object.metadata.ppuser)
        stripe_payment = Payment(
            stripe_ref = stripe_paymentintent_success.data.object.id,
            amount = stripe_paymentintent_success.data.object.amount,
            user = ppuser,
        )
        stripe_payment.save()
    except:
        return HttpResponseBadRequest()
    return HttpResponse("Confirmation for payment {} recieved by Purple Pages successfully.".format(stripe_paymentintent_success.data.object.id))