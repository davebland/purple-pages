from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Subscription, Payment

@login_required
def subscription_overview(request):
    """ Generate page showing an overview of the user's subscription """
    try:
        user_subscription = Subscription.objects.get(user=request.user)        
    except:
        user_subscription = None
    return render(request, 'subscription_overview.html', 
                    {'page_title':'My Subscription',
                    'user_subscription':user_subscription }
                )