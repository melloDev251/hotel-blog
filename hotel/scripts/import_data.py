from hotel.models import Hotel
def run():
    for i in range(6, 12):
        hotel = Hotel()
        hotel.title = "Hotel N° #%d" % i
        hotel.desc = "Description hotel N° #%d" % i
        hotel.image = "http://default"
        hotel.save()
print("Opération réussie!!") 