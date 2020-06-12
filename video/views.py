from django.shortcuts import render
from .forms import TextForm
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from .vid import getVidURL

def home(request):
    submitbutton = request.POST.get("submit")
    text_value = ''
    vid_url = {}

    form = TextForm(request.POST or None)
    if form.is_valid():
        text_value = form.cleaned_data.get("text_value")
        vid_url = getVidURL(text_value)
        form = TextForm()

    context = {'form': form, 'text_value': text_value,
               'submitbutton': submitbutton, 'vid_url': vid_url}

    return render(request, 'video/home2.html', context )
