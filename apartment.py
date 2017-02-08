from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from models.apartment import Location

# def _get_office_location(my_address):
#     geolocator = Nominatim()
#     try:
#         location = geolocator.geocode(my_address, timeout=None)
#         return Location(location.latitude, location.longitude)
#     except GeocoderTimedOut as e:
#         print("Error: geocode failed on input %s with message %s"%(my_address, e.msg))

def _get_office_address():
    geolocator = Nominatim()
    location = geolocator.reverse("52.509669, 13.376294")
    print(location.address)


#
#
# apt_list = list()
#
# def _get_apt_list(my_site, my_area, max):
#     cl_h = CraigslistHousing(site=my_site, area=my_area, category='roo',
#                              filters={'private_room': True, 'has_image': True})
#
#     count = 0
#     for result in cl_h.get_results(sort_by='newest', geotagged=True):
#         count += 1
#         if count >= max:
#             break
#         else:
#             print(result)
#             #apt_list.append(Apartment(result))

def main():
    #address = 'Vancouver,BC V6B 0M3,Canada'
    # address = "175 5th Avenue NYC"
    # location = Location(49.246292, -123.116226)
    # print(_get_office_address())

    # geolocator = Nominatim()
    # location = geolocator.reverse("52.509669, 13.376294")
    # print(location.address)

    _get_office_address()




if __name__ == '__main__':
    main()