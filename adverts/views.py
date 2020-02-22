from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Advert
from .forms import AdvertForm

@login_required
def advert_add_edit(request, advert_id=None):
    """ Generate add/edit page """

    def save_advert(request, advert_id):
        """ Create a new form instance with the post data and save if valid """
        if advert_id:
            # An existing advert to update the existing instance
            save_form = AdvertForm(request.POST, request.FILES, instance=Advert.objects.get(pk=advert_id))
        else: 
            # A new advert therefore add the current user to the POST data
            post_data = request.POST.copy()            
            post_data['ppuser'] = request.user
            save_form = AdvertForm(post_data, request.FILES)            
        
        if save_form.is_valid():         
            save_form.save()
            messages.success(request, 'Advert {} created/updated successfully'.format(save_form.cleaned_data['title']))
            return redirect('my_ads')
        else:
            return render(request, 'advert_add_edit.html', {'advert_form':save_form})

    def edit_advert(request, advert_id):
        """ Get and advert and pass it to add_edit page as form """
        # Get the object only if the authenticated user is that same as the adverts user
        advert = get_object_or_404(Advert, pk=advert_id, ppuser=request.user)
        advert_form = AdvertForm(instance=advert)
        return render(request, 'advert_add_edit.html', {'advert_form':advert_form})

    if request.method == "POST":
        return save_advert(request, advert_id)
    elif advert_id:
        return edit_advert(request, advert_id)
    else:
        # If a new advert create a blank form and pass this into template
        advert_form = AdvertForm()
        return render(request, 'advert_add_edit.html', {'advert_form':advert_form})

@login_required
def preview_advert(request):
    """ Return html preview of an advert using POST data """
    if request.method != "POST":
        return HttpResponseBadRequest()
    # Create and return an advert using the posted data with user as owner
    post_data = request.POST.copy()            
    post_data['ppuser'] = request.user     
    posted_data_into_form = AdvertForm(post_data, request.FILES)
    if posted_data_into_form.is_valid():           
        preview_advert = posted_data_into_form.save(commit=False)
        return HttpResponse(preview_advert.render())
    else:
        return HttpResponseBadRequest(posted_data_into_form.errors)