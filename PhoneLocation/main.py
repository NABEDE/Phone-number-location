import phonenumbers

from myNumber import *

from phonenumbers import geocoder

import folium

key = '4d5a8a51ea9e47889e6a71d9b71fb61b'

sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, 'fr')
print(yourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

##Save map in html file

myMap.save("myLocation.html")
