from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages

from adverts.models import Advert
from .forms import PPUserCreationForm
from .stripe import stripe_payment_intent

@login_required
def my_account(request):
    """ Generate user account overview page """

    user_stats = {
        'date_joined' : "-",
        'subscription' : 0,
        'no_of_ads' : 0,
        'total_add_views' : 0,
    }
    try:
        # Collect user stats
        user_stats['date_joined'] = request.user.date_joined.strftime("%d %b %Y")
        user_stats['subscription'] = request.user.subscription_status()
        user_stats['no_of_ads'] = Advert.objects.filter(ppuser=request.user).count()
        user_total_add_views = Advert.objects.filter(ppuser=request.user).aggregate(Sum('view_counter'))
        user_stats['total_add_views'] = user_total_add_views['view_counter__sum']
    except:
        messages.warning(request, 'Unable to load user stats')

    return render(request, 'my_account.html', {'user_stats':user_stats})

@login_required
def my_ads(request):
    """ Generate page showing all the ads for the authenticated user """
    user_ads = Advert.objects.filter(ppuser=request.user)
    if (request.user.subscription_status() == 0) or (request.user.subscription_status() == 2):
        messages.warning(request, "You do not have a active subscription so your ads are not public at the moment.")
    return render(request, 'my_ads.html', {'adverts':user_ads})

def user_registration(request):
    """ Generate a form to register a user and handle that form submission """
    if request.method == "POST":
        # Bind a form and check if valid        
        registration_form = PPUserCreationForm(request.POST)
        if registration_form.is_valid():
            # Add user and log them in
            new_user = registration_form.save()
            login(request, new_user)
            messages.success(request, "Registration successful, welcome to Purple Pages <strong>{}<strong>.".format(new_user.get_short_name()))
            return redirect('my_account')
        else:
            return render(request, 'registration.html', {'registration_form':registration_form})
        
    return render(request, 'registration.html', {'registration_form':PPUserCreationForm()})

@login_required
def my_subscription(request):
    """ Generate users subscription page """
    return render(request, 'my_subscription.html')

@login_required
def create_subscription_payment(request, subscription_period=60):
    """ Create and a return a payment intent """
    # Convert subscription period to a cost and return a payment intent for that cost
    subscription_cost = subscription_period # *multiplier if not 1p per day
    return stripe_payment_intent(payment_amount=subscription_cost, ppusername=request.user.username)