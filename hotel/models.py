from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categorie(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
        

class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my-hotel1")
