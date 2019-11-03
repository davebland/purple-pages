from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Advert
from .forms import AdvertForm

def get_ads(board_pk):
    """ Return a tuple containing all adverts for specified board """
    all_ads = Advert.objects.filter(on_boards=board_pk)
    return tuple(all_ads)

def get_user_ads(uid):
    """ Return a tuple containing all adverts with edit frames for specified user """
    # Get the adverts
    user_ads = Advert.objects.filter(user=uid)
    # Rended each to html string with edit frame
    user_ads_html = []
    for ad in user_ads:
        user_ads_html.append(render_to_string('advert_edit_frame.html', {'ad':ad}))
    return tuple(user_ads_html)

@login_required
def advert_add_edit(request, advert_id=None):
    """ Generate add/edit page """

    def save_advert(request, advert_id):
        """ Create a new form instance with the post data and save if valid """
        if advert_id:
            save_form = AdvertForm(request.POST, instance=Advert.objects.get(pk=advert_id))
        else:
            save_form = AdvertForm(request.POST)
        
        if save_form.is_valid():           
            save_form.save()
            return redirect('my_ads')
        else:
            return render(request, 'advert_add_edit.html', {'page_title':'Update Advert', 'advert_form':save_form})


    def edit_advert(request, advert_id):
        """ Get and advert and pass it to add_edit page as form """
        # Get the object only if the authenticated user is that same as the adverts user
        advert = get_object_or_404(Advert, pk=advert_id, user=request.user)
        advert_form = AdvertForm(instance=advert)
        return render(request, 'advert_add_edit.html', {'page_title':'Edit Advert', 'advert_form':advert_form})

    if request.method == "POST":
        return save_advert(request, advert_id)
    elif advert_id:
        return edit_advert(request, advert_id)
    else:
        # If a new advert create a blank form and pass this into template
        advert_form = AdvertForm(initial={'user': request.user})
        return render(request, 'advert_add_edit.html', {'page_title':'New Advert', 'advert_form':advert_form})