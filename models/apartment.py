# class Apartment(object):
#     def __init__(self, result):
#         self.name = result['name']
#         self.url = result['url']
#         if result['price'] is None:
#             self.price = 0
#         else:
#             self.price = result['price']
#         self.geotag = result['geotag']
#
#     def __dist__(self, location):
#         return 1

class Location(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude