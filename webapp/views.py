from django.shortcuts import render

from sponsors.models import Sponsor, Category, SponsorCategoryYear
from gallery.models import Image
from festival.models import Band, Year, BandYear


def home(request):
    sponsors = Sponsor.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    bands = Band.objects.all()
    years = Year.objects.all() 

    return render(request, 'index.html', {
        'sponsors':sponsors,
        'categories':categories,
        'images':images,
        'bands':bands,
        'years':years})
