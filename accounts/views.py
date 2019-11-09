from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from adverts.views import get_user_ads
from adverts.models import Advert
from subscriptions.models import Subscription

@login_required
def my_account(request):
    """ Generate user account overview page """
    # Collect some object to use in stats
    try:
        user_subscription = Subscription.objects.get(user=request.user)
    except:
        user_subscription = "No Subscription"
    try:
        user_ads = Advert.objects.filter(user=request.user).count()
    except:
        user_ads = "No Ads"
    # Create stats dict and render
    user_stats = {
        'subscription' : user_subscription,
        'no_of_ads' : user_ads,
    }
    return render(request, 'my_account.html', {'page_title':'Account Overview', 'user_stats':user_stats})

@login_required
def my_ads(request):
    """ Generate page showing all the ads for the authenticated user """
    return render(request, 'my_ads.html', {'page_title':'My Adverts', 'user_ads':get_user_ads(request.user)})