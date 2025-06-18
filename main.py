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
truck1_packages = [1, 4, 13, 14, 15, 19, 20, 21, 16, 29, 30, 31, 34, 37, 40]

# Truck 2 contained packages that were delayed until 9:05
# Also contained packages that were required to go on truck 2
# Additional packages added that either needed to arrive by 10:30, or had same address as packages already on truck
# Fewer packages to ensure time constraints met
truck2_packages = [3, 5, 6, 18, 25, 26, 28, 32, 36, 38]

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

# Sending Truck 1 to delivery packages at open (8:00 AM)
truck1.deliver_packages(datetime.time(8, 0, 0), address_lookup, distance_matrix)

# Sending Truck 2 to deliver packages after delayed packages arrive (9:05 AM)
truck2.deliver_packages(datetime.time(9,5,0), address_lookup, distance_matrix)

# Sending Truck 3 to deliver packages at earliest time driver is available after 10:20 AM to allow package 9 to receive correct address
if datetime.time(10,20,0) >= truck1.return_time or datetime.time(10,20,0) >= truck2.return_time:
    truck3.deliver_packages(datetime.time(10,20,0), address_lookup, distance_matrix)
#
elif truck2.return_time > truck1.return_time:
    truck3.deliver_packages(truck1.return_time, address_lookup, distance_matrix)
else:
    truck3.deliver_packages(truck2.return_time, address_lookup, distance_matrix)



# User Interface Function called to allow interactively looking up statistics
def user_interface():
    running = True
    daily_mileage = f"{(truck1.mileage + truck2.mileage + truck3.mileage):.1f}"


    print("Welcome to the Western Governor's University Parcel Service")
    print("")
    print("All deliveries have concluded for the day.")
    print(f"All trucks returned to hub by {truck3.return_time.strftime("%I:%M:%S %p")}")
    print(f"Total mileage for all trucks today: {daily_mileage} miles")
    print("")
    print("-" * 80)

    while running:
        print("-" * 80)

        print("MENU")
        print("Options:")
        print("1. View end of day stats")
        print("2. View Stats by Time")
        print("3. Quit")
        menu_selection = input("Enter the number corresponding to your selection (1, 2, or 3)\n")
        print("-" * 80)

        if int(menu_selection) == 1:
            print("Today's Daily Report")
            print(f"Total Mileage Driven: {daily_mileage}")
            print("\n")
            print("-" * 80)
            print("Truck Statistics")
            print(f"""
                Truck 1 Statistics:
                Miles Driven Today: {truck1.mileage:.1f}
                Departure Time: {truck1.departure_time.strftime("%I:%M:%S %p")}
                Return Time: {truck1.return_time.strftime("%I:%M:%S %p")}
                Number of Packages Delivered: {len(truck1_packages)}
                Packages Delivered: {truck1_packages}
                """)
            print(f"""
                Truck 2 Statistics:
                Miles Driven Today: {truck2.mileage:.1f}
                Departure Time: {truck2.departure_time.strftime("%I:%M:%S %p")}
                Return Time: {truck2.return_time.strftime("%I:%M:%S %p")}
                Number of Packages Delivered: {len(truck2_packages)}
                Packages Delivered: {truck2_packages}
                """)
            print(f"""
                Truck 3 Statistics:
                Miles Driven Today: {truck3.mileage:.1f}
                Departure Time: {truck3.departure_time.strftime("%I:%M:%S %p")}
                Return Time: {truck3.return_time.strftime("%I:%M:%S %p")}
                Number of Packages Delivered: {len(truck3_packages)}
                Packages Delivered: {truck3_packages}
                """)

            print("\n")
            print("-" * 80)
            print("Package Statistics")
            for i in range(1, 41):
                print(f"{package_table.lookup(i)}")

            back_to_menu = input("Back to menu? (Y/N)")

            if back_to_menu.upper() == "Y":
                continue

            elif back_to_menu.upper() == "N":
                break
            else:
                raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")

        elif int(menu_selection) == 2:
            print("-" * 80)
            print("Specify Report Time")
            time_selector = input("Enter Time: (HH:MM) \n")
            try:
                time = time_selector.split(":")
                if len(time) != 2:
                    raise ValueError("Invalid input: Input must be in format HH:MM")
                else:
                    hour = int(time[0])
                    minute = int(time[1])
            except:
                raise ValueError("Invalid input: Input must be in format HH:MM")

            if hour >= 0 and hour < 24:
                if hour >= 1 and hour <= 12:
                    if minute < 0 or minute > 59:
                        raise ValueError("Invalid time input")
                    am_pm_selector = input("AM or PM? (AM/PM)\n")
                    if am_pm_selector.upper() == "PM":
                        if hour < 12:
                            hour += 12
                    elif am_pm_selector.upper() == "AM":
                        if hour == 12:
                            hour = 0
                    else:
                        raise ValueError("Invalid input")
                else:
                    raise ValueError("Minutes must be in range 0-59, inclusive")
            else:
                raise ValueError("Hours must be in range 0-23, inclusive")


            time = datetime.time(hour, minute)
            print("-" * 80)
            print(f"You have selected {time.strftime("%I:%M:%S %p")}.")
            print("SELECT REPORT")
            print("1. View Single Package")
            print("2. View Single Truck")
            print("3. View All Trucks/Packages")
            report_selector = input("INPUT REPORT NUMBER (1-3) \n")

            if int(report_selector) == 1:
                print("-" * 80)
                print("SINGLE PACKAGE REPORT")
                print(f"Specify package to view package information at {time.strftime("%I:%M:%S %p")}")
                package_selector = input("ENTER PACKAGE ID (1-40)\n")
                if int(package_selector) in range(1, 41):
                    print(f"INFORMATION FOR PACKAGE {package_selector}")
                    print(package_table.lookup(int(package_selector), time))
                else:
                    raise ValueError("Invalid input: Input must be a number in range 1-40, inclusive")

                back_to_menu = input("Back to menu? (Y/N)")

                if back_to_menu.upper() == "Y":
                    continue

                elif back_to_menu.upper() == "N":
                    break
                else:
                    raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")

            if int(report_selector) == 2:
                print("-" * 80)
                print("SINGLE TRUCK REPORT")
                print(f"Specify truck to see truck information at {time.strftime("%I:%M:%S %p")}")
                truck_selector = input("INPUT TRUCK ID (1-3)\n")

                if int(truck_selector) not in range(1, 4):
                    raise ValueError("Invalid input: Input must be an integer in range 1-3, inclusive")
                else:
                    if int(truck_selector) == 1:
                        print(f"Viewing Truck 1 at {time.strftime("%I:%M:%S %p")}\n")
                        print(f"Mileage: {truck1.mileage_at_time(time):.1f} miles")
                        print(f"Package Stats for Package IDs assigned to Truck 1: {truck1_packages}")
                        for p in truck1_packages:
                            print(package_table.lookup(p, time))
                        back_to_menu = input("Back to menu? (Y/N)")

                        if back_to_menu.upper() == "Y":
                            continue

                        elif back_to_menu.upper() == "N":
                            break
                        else:
                            raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")


                    elif int(truck_selector) == 2:
                        print(f"Viewing Truck 2 at {time.strftime("%I:%M:%S %p")}\n")
                        print(f"Mileage: {truck2.mileage_at_time(time):.1f} miles")
                        print(f"Package Stats for Package IDs assigned to Truck 2: {truck2_packages}")
                        for p in truck2_packages:
                            print(package_table.lookup(p, time))
                        back_to_menu = input("Back to menu? (Y/N)")

                        if back_to_menu.upper() == "Y":
                            continue

                        elif back_to_menu.upper() == "N":
                            break
                        else:
                            raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")


                    elif int(truck_selector) == 3:
                        print(f"Viewing Truck 3 at {time.strftime("%I:%M:%S %p")}\n")
                        print(f"Mileage: {truck3.mileage_at_time(time):.1f} miles")
                        print(f"Package Stats for Package IDs assigned to Truck 3 {truck3_packages}")
                        for p in truck3_packages:
                            print(package_table.lookup(p, time))
                        back_to_menu = input("Back to menu? (Y/N)")

                        if back_to_menu.upper() == "Y":
                            continue

                        elif back_to_menu.upper() == "N":
                            break
                        else:
                            raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")

            if int(report_selector) == 3:
                print(f"ALL TRUCKS/PACKAGES AT {time.strftime("%I:%M:%S %p")}\n")
                print("\n")
                print(f"Total Mileage driven at {time.strftime("%I:%M:%S %p")}: {(truck1.mileage_at_time(time) + truck2.mileage_at_time(time) + truck3.mileage_at_time(time)):.1f}")
                print("**********")
                print(f"Viewing Truck 1 at {time.strftime("%I:%M:%S %p")}\n")
                print(f"Mileage: {truck1.mileage_at_time(time):.1f} miles")
                print(f"Package Stats for Package IDs assigned to Truck 1: {truck1_packages}")
                for p in truck1_packages:
                    print(package_table.lookup(p, time))
                print("**********")
                print(f"Viewing Truck 2 at {time.strftime("%I:%M:%S %p")}\n")
                print(f"Mileage: {truck2.mileage_at_time(time):.1f} miles")
                print(f"Package Stats for Package IDs assigned to Truck 2: {truck2_packages}")
                for p in truck2_packages:
                    print(package_table.lookup(p, time))
                print("***********")
                print(f"Viewing Truck 3 at {time.strftime("%I:%M:%S %p")}\n")
                print(f"Mileage: {truck3.mileage_at_time(time):.1f} miles")
                print(f"Package Stats for Package IDs assigned to Truck 3 {truck3_packages}")
                for p in truck3_packages:
                    print(package_table.lookup(p, time))
                back_to_menu = input("Back to menu? (Y/N)")

                if back_to_menu.upper() == "Y":
                    continue

                elif back_to_menu.upper() == "N":
                    break
                else:
                    raise ValueError("Invalid input; Valid inputs are 'Y' and 'N' - exiting program")

        elif int(menu_selection) == 3:
            print("Goodbye!")
            break














user_interface()
