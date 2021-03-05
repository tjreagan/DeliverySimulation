# Thomas Reagan
# ID: 001265074

# Class for location objects that are used as inputs
# in distance functions throughout the program
class Location:
    def __init__(self, location_id, name, address, zip_code, distances):
        self.location_id = location_id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.distances = distances

    # This function is used to assign locations to any packages
    # that have a matching location. It's easier to have a full
    # location object associated with a package than to have to
    # compare address strings when referencing the distance table
    # O(1)
    def get_matching_package(self, inventory, key):
        if inventory.search(key).address == self.address:
            package = inventory.search(key)
            return package
        else:
            pass

# Compares two locations to grab a particular distance value
# O(1)
def get_distance(locations, location_a, location_b):
    if locations.index(location_a) > locations.index(location_b):
        distance = float(location_a.distances[locations.index(location_b)])
        return distance
    else:
        distance = float(location_b.distances[locations.index(location_a)])
        return distance

# Function able to retrieve a location object using an
# address string value
# O(n)
def get_matching_location(locations, address):
    for i in range(len(locations)):
        if address == locations[i].address:
            return locations.index(locations[i])
        else:
            pass

