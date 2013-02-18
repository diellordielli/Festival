from django.shortcuts import render

from sponsors.models import Sponsor, Category
from gallery.models import Image
from festival.models import Band, BandYear, BandLinks, Year
from news.models import News
from mood.models import Mood


def home(request):
    sponsors = Sponsor.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    bands = Band.objects.all()
    bandyears = BandYear.objects.all()
    bandlinks = BandLinks.objects.all()
    newss = News.objects.all()
    moods = Mood.objects.all()
    years = Year.objects.all()
    return render(request, 'index.html', {
        'sponsors': sponsors,
        'categories': categories,
        'images': images,
        'bands': bands,
        'bandyears': bandyears,
        'bandlinks': bandlinks,
        'newss': newss,
        'moods': moods,
        'years': years,
        })
