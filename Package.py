# Thomas Reagan
# ID: 001265074

from Time import *

# Class for the package objects
class Package:
    #Typical constructor to set default values using inputs from the csv file
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass, special_note, location):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.special_note = special_note
        self.delivery_status = "At Hub"
        self.location = location

    # Function to change the delivery status
    def on_truck(self):
        self.delivery_status = "On Truck"

    # Function to change the delivery status
    def delivered(self, time):
        time_delta = time.total_seconds
        self.delivery_status = "Delivered at " + str(time.time)

    # Function to return the delivery status
    def get_delivery_status(self):
        return self.delivery_status
