from datetime import datetime

from django.shortcuts import render


from .sponsors.models import Sponsor, Category
from .gallery.models import Image
from .festival.models import Band, BandYear, BandLinks, Year
from .news.models import News
from .mood.models import Mood


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
    now = datetime.now()
    thisyears = Year.objects.filter(year=now.year)
    yearcovers = Image.objects.filter(is_yearcover=True).order_by("year__year")

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
        'thisyears': thisyears,
        'yearcovers': yearcovers,
        })


def get_band(request, band):
    band = Band.objects.get(slug=band)

    return render(request, 'bandsingle.html', {
        'band': band,
        })
