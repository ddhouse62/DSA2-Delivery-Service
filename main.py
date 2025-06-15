# Dalton  House - Student ID 009453254 - WGU C950
import csv
import datetime
from hash_table import HashTable
from package import Package
from truck import Truck


# Create Hash Table instance to hold packages in main
package_table = HashTable()

# Import csv containing package data
with open('package_file.csv') as package_file:
    package_reader = csv.reader(package_file, delimiter=',')
    next(package_reader)

    # Each row in csv represents a new package - iterate over each row to gain attributes
    for row in package_reader:
        package_id = int(row[0])
        package_address = row[1]
        package_city = row[2]
        package_zipcode = row[3]
        package_weight = row[4]
        package_deadline = row[5]

        # Store each package in a package object - each attribute is assigned to one of the rows
        pack = Package(package_id, package_address, package_city, package_zipcode, package_weight, package_deadline)
        package_table.insert(package_id, pack)

# Initialize empty list to hold distance matrix
distance_matrix = []

# Initialize empty dictionary to map locations to indexes for fast indexing
address_lookup = []

with open('distance_table.csv', newline = '') as distance_table:
    distance_reader = csv.reader(distance_table, delimiter = ',')
    address_lookup = next(distance_reader)
    for row in distance_reader:
        distance_matrix.append(row)

# Update Package 9 address at 10:20 am
package_table.insert(9, Package(9,'410 S State St', 'Salt Lake City', '84111', 'EOD', '2'))

# Truck 1 Packages identified all packages to be delivered before 10:30 that were not delayed.
# Additionally, included packages that had to be delivered together
# Finally, remaining packages determined by adding packages delivered to same address as packages that meet other constraints
truck1_packages = [1, 4, 13, 14, 15, 19, 20, 21, 16, 29, 30, 31, 32, 34, 37, 40]

# Truck 2 contained packages that were delayed until 9:05
# Also contained packages that were required to go on truck 2
# Additional packages added that either needed to arrive by 10:30, or had same address as packages already on truck
# Fewer packages to ensure time constraints met
truck2_packages = [3, 5, 6, 18, 25, 26, 28, 36, 38]

# Truck 3 contains packages not on trucks 1 and 2
# Package 9 included on this truck to account for change in address
truck3_packages = [2, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39]

# Initialize and load each truck
truck1 = Truck(1)
truck1.load_packages(truck1_packages, package_table)


truck2 = Truck(2)
truck2.load_packages(truck2_packages, package_table)


truck3 = Truck(3)
truck3.load_packages(truck3_packages, package_table)


# Deliver packages for each truck
truck1.deliver_packages(datetime.time(8, 0, 0), address_lookup, distance_matrix)
truck2.deliver_packages(datetime.time(9,5,0), address_lookup, distance_matrix)
truck3.deliver_packages(datetime.time(10,20,0), address_lookup, distance_matrix)

def user_interface():
    print("Welcome to the Western Governor's University Parcel Service")
    print("")
    print("All deliveries have concluded for the day.")
    print(f"All trucks returned to hub by {truck3.return_time.strftime("%I:%M:%S %p")}")
    print(f"Total mileage for all trucks today: {truck1.mileage + truck2.mileage + truck3.mileage} miles")
    print("")
    print("")
    print("Menu - Select the number for the function ")
    print("1. View end of day stats")
    print("2. Specify Time")
    print("3. Quit")
    menu_selection = input("Enter the number corresponding to your selection (1-3)")

    if menu_selection == 1:
        print("Today's Daily Report")
        print(daily_report())


user_interface()
