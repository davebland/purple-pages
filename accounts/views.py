from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def my_account(request):
    return render(request, 'my_account.html', {'page_title':'Account Overview'})

@login_required
def my_ads(request):
    return render(request, 'my_ads.html', {'page_title':'My Adverts'})