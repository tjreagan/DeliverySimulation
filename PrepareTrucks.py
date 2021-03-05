# Thomas Reagan
# ID: 001265074

from Manifest import *

# Function used to predetermine all three truckloads of
# packages. Designed to prioritze packages with regards
# to the contents of their deadlines and special notes
# O(n)
def prepare_trucks(package_list, manifest):

    all_keys = []

    #Populates a list of all keys
    for i in range(len(package_list)):
        all_keys.append(package_list[i].package_id)

    truck_one = []
    truck_two = []
    truck_three = []

    packages_must_together = [13, 14, 15, 16, 19, 20]
    packages_with_deadline = []
    packages_delayed = []
    truck_two_only = []
    others = []

    # Remove predetermined set from all keys
    for i in packages_must_together:
        all_keys.remove(i)

    for i in all_keys:
        package_to_check = manifest.search(i)
        note = package_to_check.special_note
        deadline = package_to_check.deadline

        if i == 9:
            truck_three.append(i)
        elif note.__contains__('Can only'):
            truck_two.append(i)
        elif note.__contains__('Delayed'):
            truck_two.append(i)
        elif deadline.__contains__('9:00 AM'):
            truck_one.append(i)
        elif deadline.__contains__('10:30 AM'):
            packages_with_deadline.append(i)
        else:
            others.append(i)

    truck_one += packages_must_together
    truck_one += packages_with_deadline

    for i in others:
        if len(truck_one) == 16:
            break
        else:
            truck_one.append(i)
            others.remove(i)

    for i in others:
        if len(truck_two) == 16:
            break
        else:
            truck_two.append(i)
            others.remove(i)

    truck_three += others

    return truck_one, truck_two, truck_three

