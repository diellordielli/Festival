from datetime import datetime

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .sponsors.models import Sponsor, Category, SponsorCategoryYear
from .gallery.models import Image
from .festival.models import Band, BandYear, BandLinks, Year
from .news.models import News
from .mood.models import Mood
from .contact.models import Contact, Person


def home(request):
    now = datetime.now()
    current_year = Year.objects.get(year=now.year)
    sponsors = Sponsor.objects.all()
    sponsors = Sponsor.objects.filter(years=current_year).order_by('sponsorcategoryyear__category')
    categories = Category.objects.all()
    sponsorcategoryyears = SponsorCategoryYear.objects.all()
    images = Image.objects.all()
    bands = Band.objects.filter(years=current_year).order_by('bandyear__time')
    bandyears = BandYear.objects.all()
    bandlinks = BandLinks.objects.all()
    newss = News.objects.all()
    mood = Mood.objects.latest('id')
    years = Year.objects.all()
    thisyears = Year.objects.filter(year=now.year)
    yearcovers = Image.objects.filter(is_yearcover=True).order_by("year__year")
    contacts = Contact.objects.all()
    persons = Person.objects.all()

    return render(request, 'index.html', {
        'sponsors': sponsors,
        'categories': categories,
        'sponsorcategoryyears': sponsorcategoryyears,
        'images': images,
        'bands': bands,
        'bandyears': bandyears,
        'bandlinks': bandlinks,
        'newss': newss,
        'mood': mood,
        'years': years,
        'thisyears': thisyears,
        'yearcovers': yearcovers,
        'contacts': contacts,
        'persons': persons,
    })


def get_band(request, band):
    band = Band.objects.get(slug=band)
    now = datetime.now()
    thisyears = Year.objects.filter(year=now.year)
    images = Image.objects.all()
    bandyears = BandYear.objects.all()

    return render(request, 'bandsingle.html', {
        'band': band,
        'thisyears': thisyears,
        'images': images,
        'bandyears': bandyears,
    })


def get_gallery(request, year):
    now = datetime.now()
    year = Year.objects.get(year=year)
    images = year.image_set.all()
    thisyears = Year.objects.filter(year=now.year)
    bandlinks = BandLinks.objects.all()

    return render(request, 'gallery.html', {
        'images': images,
        'thisyears': thisyears,
        'bandlinks': bandlinks,
    })


def contact(request):
    message = ''

    if request.method == 'POST':
        post = request.POST.copy()

        post.pop('csrfmiddlewaretoken')
        for entry in post:
            message += entry + ':\n'
            message += post[entry].strip() + '\n\n'

        send_mail(
            'Neue Formulareingabe %s auf stolze-openair.ch' % post['Formular'],
            message,
            'bot@stolze-openair.ch',
            ['dd@feinheit.ch', 'mail@stolze-openair.ch'],
            fail_silently=False)
        return HttpResponseRedirect('/thanks/')
    return HttpResponseRedirect('/')


def thanks(request):
    return render(request, 'thanks.html', {
    })
