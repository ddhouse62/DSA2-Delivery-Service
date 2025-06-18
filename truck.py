import routing
import datetime

# implement a truck class to carry packages for delivery

# Capacity and speed are both constants and are not modified, will not be accessible by user by default
CAPACITY = 16
SPEED = 18

class Truck:
    def __init__(self, id, mileage = 0):
        # Each truck will be identified by their ID
        self.id = id
        # Demonstrates current mileage of truck object
        self.mileage = mileage

        # Each truck's capacity will be set to the capacity object
        self.capacity = CAPACITY

        # Initialize packages as empty list, and any packages identified in constructor are loaded at this time, assuming less than capacity
        self.packages = []

        # Truck Speed will be set to speed constant (18 mph in this instance)
        self.speed = SPEED

        # Truck departure time identified by delivery method
        self.departure_time = None

        # Truck return time identified during delivery
        self.return_time = None


    # Method to load trucks with list of packages
    # Packages are pulled from specified hash table using existing method
    def load_packages(self, package_ids, package_table):
        if len(self.packages) + len(package_ids) <= self.capacity:
            for p in package_ids:
                self.packages.append(package_table.search(p))
        else:
            raise ValueError(f"Packages on Truck cannot exceed {self.capacity}.\nCurrent Load: {len(self.packages)}.\nNumber of packages attempted to be loaded: {len(package_ids)}.")

    # Returns a list of addresses to deliver to based on packages currently on the truck
    def get_addresses(self):
        addresses = []
        for p in self.packages:
            addresses.append(p.address)
        return addresses

    # Returns a list of packages identified by their package_id
    def get_packages(self):
        package_number = []
        for p in self.packages:
            package_number.append(p.get_package_id())
        return package_number

    # Creates a dictionary, where keys are addresses in a list, while values are packages to deliver at that address
    def map_addresses_to_packages(self, addresses):
        address_to_package = {}
        for address in addresses:
            list_packages_at_address = []
            for package in self.packages:
                if package.get_address() == address:
                    list_packages_at_address.append(package)
            address_to_package[address] = list_packages_at_address
        return address_to_package


    # Method used to complete deliveries of packages
    # Sets departure time, calculates mileage of route, calculates route based on packages on truck, delivers packages, sets time for each delivered package
    # Implementation is set such that routes are calculated before delivery - this is done so that routing algorithms can be modified without re-architecting the method
    # Downsides to this method: routes are created at the beginning of the method, meaning the route is created prior to delivery - as a result, if information about the packages changes during the course of delivery, this route will not adjust
    # Limitation identified is considered acceptable for this instance, as current implementation trades efficiency for maintainability by separating the routing and delivery functions
    def deliver_packages(self, departure_time, address_lookup, distance_lookup):

        # Set departure time value for truck and packages, given as datetime for ease of arithmetic comparison
        self.departure_time = departure_time

        for p in self.packages:
            p.departure_time = departure_time

        # Hub is at WGU facility in address table, index 0
        hub = address_lookup[0]


        # Extract delivery addresses for package
        addresses = list(set(self.get_addresses()))

        # Creates a dictionary mapping each address to the packages at that address
        address_package_map = self.map_addresses_to_packages(addresses)

        # Calculate delivery route using nearest-neighbor algorithm
        route = routing.get_route(hub, addresses, address_lookup, distance_lookup)


        # Calculate distance of delivery route and append it to mileage
        route_distance = routing.get_route_distance(route, address_lookup, distance_lookup)

        self.mileage = route_distance

        # Calculate time to complete route
        time_to_complete = datetime.timedelta(hours = (float(route_distance) / float(self.speed)))

        # Specify return time for 'time' based calculations
        # Combines datetime 'time' object with datetime 'date' object to allow 'timedelta' object to be added, before converting back to 'time' object
        self.return_time = (datetime.datetime.combine(datetime.date.today(), departure_time) + time_to_complete).time()

        # Deliver packages
        # Set total distance driven for deliveries to 0
        delivery_distance = 0

        # Deliver packages on route based on addresses, set delivery times
        # Start at 2nd item in list and end at next_to_last item in list to prevent issues with item lookup
        for i in range(1, len(route) - 1):

            # set address and previous address variables for easy lookup
            address = route[i]
            previous_address = route[i - 1]


            # calculate distance driven from start of route to next address
            delivery_distance += routing.get_distance(previous_address, address, address_lookup, distance_lookup)

            # calculate time it takes to drive route to address
            time_to_address = datetime.timedelta(hours = (float(delivery_distance) / float(self.speed)))

            # using time calculated, set package delivery time to departure time + time taken to deliver
            for package in address_package_map[address]:
                package.delivery_time = (datetime.datetime.combine(datetime.date.today(), package.departure_time) + time_to_address).time()
                self.packages.remove(package)




    # Calculates the mileage traveled by a truck at a specified time
    def mileage_at_time(self, time):
        if time >= self.return_time:
            mileage = self.mileage
            return mileage
        elif time >= self.departure_time and time < self.return_time:
            time_delta = (datetime.datetime.combine(datetime.date.today(), time)) - (datetime.datetime.combine(datetime.date.today(), self.departure_time))
            td = time_delta.total_seconds() / 3600.0
            mileage = td * self.speed
            return mileage
        else:
            mileage = 0
            return mileage
