from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def my_account(request):
    return render(request, 'my_account.html')