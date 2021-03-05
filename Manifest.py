# Thomas Reagan
# ID: 001265074

import csv
from HashTable import *
from Location import *
from Package import *

# Function used to build all the necessary tables needed
# for the program. Creates a list of locations, a list of
# packages, and a hash table of packages that contain a
# location object within them
# O(n^2)
def initialize_tables(distance_csv, package_csv):
    with open(distance_csv) as distance_file:
        read_distance_file = csv.reader(distance_file, skipinitialspace=True, delimiter=',')
        locations = []

        for row in read_distance_file:
            location_id = row
            name = row[0]
            address = row[1]
            zip_code = row[2]
            distances = row[3:]
            address = address.replace('North', 'N').replace('South', 'S').replace('East', 'E').replace('West', 'W').replace('Bus', 'bus')

            locations.append(Location(location_id, name, address, zip_code, distances))

    with open(package_csv) as package_file:
        read_package_file = csv.reader(package_file, delimiter=',')
        packages = []

        for row in read_package_file:
            package_id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            mass = row[6]
            special_note = row[7]

            packages.append(Package(int(package_id), address, city, state, zip_code, deadline, mass, special_note, locations[get_matching_location(locations, address)]))

    manifest = HashTable(packages)
    for i in range(len(packages)):
        manifest.insert(packages[i].package_id, packages[i])

    return manifest, packages, locations

# Function to print the entire package list and all of their
# attributes.
# O(n)
def get_all_package_info(manifest, packages):
    for i in range(len(packages)):
        print("Package ID: " + str(manifest.search(i+1).package_id))
        print("Address: " + str(manifest.search(i+1).address))
        print("Deadline: " + str(manifest.search(i+1).deadline))
        print("City: " + str(manifest.search(i+1).city))
        print("Zip Code: " + str(manifest.search(i+1).zip_code))
        print("Weight: " + str(manifest.search(i+1).mass))
        print("Delivery Status: " + str(manifest.search(i+1).delivery_status) + "\n")

def get_single_package(manifest, package_id):
    print("Package ID: " + str(manifest.search(package_id).package_id))
    print("Address: " + str(manifest.search(package_id).address))
    print("Deadline: " + str(manifest.search(package_id).deadline))
    print("City: " + str(manifest.search(package_id).city))
    print("Zip Code: " + str(manifest.search(package_id).zip_code))
    print("Weight: " + str(manifest.search(package_id).mass))
    print("Delivery Status: " + str(manifest.search(package_id).delivery_status) + "\n")
