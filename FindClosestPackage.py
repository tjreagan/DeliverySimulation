# Thomas Reagan
# ID: 001265074

from Location import *
from Manifest import *

# Function to find the closest location using an
# existing location, an inventory list of id's, and
# the main manifest hash table
# O(n)
def find_closest_package(current_location, key_list, manifest, locations):

    distance = 100
    inventory_locations = []
    best_location = None
    best_key = None

    # Since the get_distance function takes two locations
    # as input, the key list is used to create a list of
    # corresponding locations from their respective match in
    # the manifest hash table
    for i in key_list:
        inventory_locations.append(manifest.search(i).location)

    # Checks each location in the list against the current location
    # and returns the lowest value (i.e. the closest location)
    for i in range(len(inventory_locations)):
        if get_distance(locations, current_location, inventory_locations[i]) == 0:
            distance = 0
            best_location = current_location
            best_key = key_list[i]
        elif get_distance(locations, current_location, inventory_locations[i]) < distance:
            distance = get_distance(locations, current_location, inventory_locations[i])
            best_location = inventory_locations[i]
            best_key = key_list[i]
        else:
            pass

    return distance, best_location, best_key

