from django.shortcuts import render
from .models import Hotel

def home(request):
    list_hotels = Hotel.objects.all()
    context = {"liste_hotels": list_hotels}
    return render(request, "index.html", context)

def detail(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    categorie = hotel.categorie
    articles_en_relation = Hotel.objects.filter(categorie=categorie)[:7]
    context = {"hotels": hotel, "her": articles_en_relation}
    return render(request, "detail.html", context)

def search(request):
    query = request.GET["hotel"]
    search_hotel = Hotel.objects.filter(title__contains=query)
    context = {"searchs_hotel": search_hotel}
    return render(request, "search.html", context)

def contact(request):
    return render(request, "contact.html")
