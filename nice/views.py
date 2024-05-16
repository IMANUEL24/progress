from django.shortcuts import render
from .models import Listing
# Create your views here.

def listings_list(request):
    listingss = Listing.objects.all()
    context = {
        "listingss":listingss
    }
    return render(request, "home.html", context)