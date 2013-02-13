from django.shortcuts import render

from sponsors.models import Sponsor, Category, SponsorCategoryYear
from gallery.models import Image


def home(request):
    sponsors = Sponsor.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'index.html', {'sponsors':sponsors, 
        'categories':categories, 'images':images})
