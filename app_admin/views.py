from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from hotel.models import Hotel
from hotel.forms import HotelForm

def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def user_hotels(request): 
    list_hotels = Hotel.objects.filter(user=request.user)
    context = {"liste_hotels": list_hotels}
    return render(request, "my_hotel.html", context)

class addHotel(LoginRequiredMixin, CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = "add_hotel.html"
    success_url = "my-hotel"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class updateHotel(LoginRequiredMixin, UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = "app_admin/hotel_form.html"


class deleteHotel(LoginRequiredMixin, DeleteView):
    model = Hotel
    success_url = "/my-admin/my-hotel"

    


