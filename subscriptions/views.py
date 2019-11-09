from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def subscription_overview(request):
    """ Generate page showing an overview of the user's subscription """
    return render(request, 'subscription_overview.html', {'page_title':'My Subscription'})