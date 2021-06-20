from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['title', 'categorie', 'desc', 'image']
        labels = {'title':'Titre', 'categorie':'Catégorie', 'desc':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'categorie':forms.Select(attrs={'class':'form-control mb-3'}),
            'desc':forms.Textarea(attrs={'class':'form-control mb-3', 'row':5, 'style':'height:150px'}),
        }