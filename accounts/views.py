from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from adverts.views import get_user_ads

@login_required
def my_account(request):
    return render(request, 'my_account.html', {'page_title':'Account Overview'})

@login_required
def my_ads(request):
    """ Generate page showing all the ads for the authenticated user """
    return render(request, 'my_ads.html', {'page_title':'My Adverts', 'user_ads':get_user_ads(4)})