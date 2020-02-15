from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages

from adverts.models import Advert

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
    return render(request, 'my_ads.html', {'page_title':'My Adverts', 'user_ads':get_user_ads(request.user)})