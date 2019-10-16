from django.shortcuts import render

def home(request):
    """ Generate Application Home Page """
    return render(request, 'home.html', {'page_title':"Welcome To Purple Pages"})

def notice_boards(request):
    """ Generate Notice Boards Page """
    return render(request, 'notice_boards.html', {'page_title':"Find Your Local Notice Board"})