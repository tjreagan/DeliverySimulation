# Thomas Reagan
# ID: 001265074

from Manifest import *
from Delivery import *
from PrepareTrucks import *

# Initialize tables
tables = initialize_tables('WGUPS Distance Table.csv', 'WGUPS Package Table.csv')
manifest = tables[0]
packages = tables[1]
locations = tables[2]

# Prepare truckloads
trucks = prepare_trucks(packages, manifest)
print(trucks[0], trucks[1], trucks[2])

# Handle user input
input_time = input("Enter a time from 00:00 to 23:59: ")

time = input_time.split(':')
hours = int(time[0])
minutes = int(time[1])
total_seconds = (hours * 60 * 60) + (minutes * 60)

input_id = input("Enter a package ID or 0 to return all packages: ")

# Run simulation
deliver_packages(trucks[0], trucks[1], trucks[2], manifest, locations, packages, total_seconds, int(input_id))