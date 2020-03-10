from django.http import JsonResponse, HttpResponseBadRequest

import os
import stripe

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

def stripe_confirm_payment(payment_confirmation):
    """ Handle successfull payment intent from Stripe """
    # Parse the POST data into JSON
    print(payment_confirmation)
    pass