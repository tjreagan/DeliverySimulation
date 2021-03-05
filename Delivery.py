# Thomas Reagan
# ID: 001265074

from Time import *
from FindClosestPackage import *
from Package import *

# The primary algorithm that handles the actual delivery of the
# truckloads. The algorithm used has elements of a divide and
# conquer approach as well as a brute force approach as it divides
# the loads to meet criteria and then simply does a search for the
# next closest package in the given list (brute force distance check)
# O(n^3)
def deliver_packages(truck_one, truck_two, truck_three, manifest, locations, packages, input_time, input_id):
    truck_one_distance = 0
    truck_two_distance = 0
    truck_one_timer = Time()
    truck_two_timer = Time()
    truck_two_timer.total_seconds = 32700
    truck_one_location = locations[0]
    truck_two_location = locations[0]

    truck_one_order = []
    truck_two_order = []

    inventory_one = truck_one
    inventory_two = truck_two
    inventory_three = truck_three
    inventory_one_priority = []
    inventory_two_priority = []

    #Prioritizing packages with deadlines on truck 2
    for i in inventory_two:
        if manifest.search(i).deadline.__contains__("10:30 AM"):
            inventory_two_priority.append(i)
            inventory_two.remove(i)
        else:
            pass

    # Driver 1's delivery. Range 2 is because he'll be the one to return
    # to the hub to get the third truckload. Depending on the input from
    # the user interface, the algorithm breaks early to return the appropriate
    # status of all packages at a given time
    # O(n^3)
    for i in range(2):
        if input_time < truck_one_timer.total_seconds:
            pass
        else:
            for n in inventory_one:
                if manifest.search(n).delivery_status.__contains__("At Hub"):
                    manifest.search(n).delivery_status = ("En route")
                else:
                    pass
        while len(inventory_one) > 0:
            if truck_one_timer.total_seconds >= input_time:
                break
            else:
                pass

            # Pre-determined location change for package 9 at the proper time.
            if truck_one_timer.total_seconds >= 37200:
                manifest.search(9).location = locations[19]
            while len(inventory_one_priority) > 0:
                # Pre-determined location change for package 9 at the proper time.
                if truck_one_timer.total_seconds >= 37200:
                    manifest.search(9).location = locations[19]
                package_to_deliver = find_closest_package(truck_one_location, inventory_one_priority, manifest, locations)
                truck_one_location = package_to_deliver[1]
                truck_one_distance += package_to_deliver[0]
                inventory_one_priority.remove(package_to_deliver[2])
                truck_one_timer.add_time(package_to_deliver[0])

                manifest.search(package_to_deliver[2]).delivered(truck_one_timer)
                truck_one_order.append(package_to_deliver[2])

                '''print(package_to_deliver[0], package_to_deliver[1].address, package_to_deliver[2])
                print("Truck 1 Total Distance: " + str(round(truck_one_distance, 2)))
                print(manifest.search(package_to_deliver[2]).get_delivery_status() + "\n")'''

            package_to_deliver = find_closest_package(truck_one_location, inventory_one, manifest, locations)
            truck_one_location = package_to_deliver[1]
            truck_one_distance += package_to_deliver[0]
            inventory_one.remove(package_to_deliver[2])
            truck_one_timer.add_time(package_to_deliver[0])

            manifest.search(package_to_deliver[2]).delivered(truck_one_timer)
            truck_one_order.append(package_to_deliver[2])

            '''print(package_to_deliver[0], package_to_deliver[1].address, package_to_deliver[2])
            print("Truck 1 Total Distance: " + str(round(truck_one_distance, 2)))
            print(manifest.search(package_to_deliver[2]).get_delivery_status() + "\n")'''

        # This block is where the changeover to the next truckload occurs
        if len(inventory_one) == 0:
            truck_one_distance += get_distance(locations, truck_one_location, locations[0])
            truck_one_location = locations[0]
            inventory_one = inventory_three
            '''print("Truck 1 Total Distance: " + str(round(truck_one_distance, 2)))
            print("Time: " + str(truck_one_timer.time) + "\n")'''

    # Same as driver 1 but with one truckload.
    # O(n^3)
    for i in range(1):
        if input_time > truck_two_timer.total_seconds:
            for n in (inventory_two + inventory_two_priority):
                if manifest.search(n).delivery_status.__contains__("At Hub"):
                    manifest.search(n).delivery_status = ("En route")
                else:
                    pass
        while len(inventory_two) > 0:
            if truck_two_timer.total_seconds >= input_time:
                break
            else:
                pass

            while len(inventory_two_priority) > 0:
                if truck_two_timer.total_seconds >= input_time:
                    break
                else:
                    pass

                truck_two_package = find_closest_package(truck_two_location, inventory_two_priority, manifest, locations)
                truck_two_location = truck_two_package[1]
                truck_two_distance += truck_two_package[0]
                inventory_two_priority.remove(truck_two_package[2])
                truck_two_timer.add_time(truck_two_package[0])

                manifest.search(truck_two_package[2]).delivered(truck_two_timer)
                truck_two_order.append(truck_two_package[2])

                '''print(truck_two_package[0], truck_two_package[1].address, truck_two_package[2])
                print("Truck 2 Total Distance: " + str(round(truck_two_distance, 2)))
                print(manifest.search(truck_two_package[2]).get_delivery_status() + "\n")'''

            truck_two_package = find_closest_package(truck_two_location, inventory_two, manifest, locations)
            truck_two_location = truck_two_package[1]
            truck_two_distance += truck_two_package[0]
            inventory_two.remove(truck_two_package[2])
            truck_two_timer.add_time(truck_two_package[0])

            manifest.search(truck_two_package[2]).delivered(truck_two_timer)
            truck_two_order.append(truck_two_package[2])

            '''print(truck_two_package[0], truck_two_package[1].address, truck_two_package[2])
            print("Truck 2 Total Distance: " + str(round(truck_two_distance, 2)))
            print(manifest.search(truck_two_package[2]).get_delivery_status() + "\n")'''

        if len(inventory_two) == 0:
            truck_two_distance += get_distance(locations, truck_two_location, locations[0])
            truck_two_location = locations[0]

            '''print("Truck 2 Total Distance: " + str(round(truck_two_distance, 2)))
            print("Time: " + str(truck_two_timer.time) + "\n")'''

    # Handles the output depending on what the user inputs
    if input_id == 0:
        print("\nDelivery status of all packages at: " + str(datetime.timedelta(0, input_time)))
        print("\n--------------------------------------------------------------")
        get_all_package_info(manifest, packages)
        print("\n--------------------------------------------------------------")
        print("Total mileage at " + str(datetime.timedelta(0, input_time)) + " is: " + str(truck_one_distance + truck_two_distance))
    else:
        print("\nDelivery status of package " + str(input_id) + "at: " + str(datetime.timedelta(0, input_time)))
        print("\n--------------------------------------------------------------")
        get_single_package(manifest, input_id)
        print("\n--------------------------------------------------------------")
        print("Total mileage at " + str(datetime.timedelta(0, input_time)) + " is: " + str(truck_one_distance + truck_two_distance))

    return truck_one_distance, truck_two_distance

