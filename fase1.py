from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geomikev2")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
