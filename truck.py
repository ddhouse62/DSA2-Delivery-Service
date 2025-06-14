import routing

# implement a truck class to carry packages for delivery

# Capacity and speed are both constants and are not modified, will not be accessible by user by default
CAPACITY = 16
SPEED = 18

class Truck:
    def __init__(self, id, packages, mileage = 0):
        # Each truck will be identified by their ID
        self.id = id
        # Demonstrates current mileage of truck object
        self.mileage = mileage

        # Each truck's capacity will be set to the capacity object
        self.capacity = CAPACITY

        # Initialize packages as empty list, and any packages identified in constructor are loaded at this time, assuming less than capacity
        self.packages = []
        if len(packages) <= self.capacity:
            for package in packages:
                self.packages.append(package)
        else:
            raise ValueError(f"Number of packages cannot exceed {self.capacity}.  Current package total: {len(self.packages)}.")

        # Truck Speed will be set to speed constant (18 mph in this instance)
        self.speed = SPEED

        # Truck departure time identified by delivery method
        self.departure_time = None

        # Truck return time identified during delivery
        self.return_time = None


    # Method to quickly load trucks with pre-defined lists of packages
    def load(self, packages_to_load):
        if len(self.packages) + len(packages_to_load) <= self.capacity:
            for package in packages_to_load:
                self.packages.append(package)
        else:
            raise ValueError(f"Packages on Truck cannot exceed {self.capacity}.\nCurrent Load: {len(self.packages)}.\nNumber of packages loaded: {len(packages_to_load)}.")

    def get_addresses(self):
        addresses = []
        for p in self.packages:
            addresses.append(p.address)
        return addresses

    # Method used to complete deliveries of packages
    def deliver_packages(self, departure_time, address_lookup, distance_lookup):
        # Set departure time value for truck and packages
        self.departure_time = departure_time
        for p in self.packages:
            p.departure_time = departure_time

        # Hub is at WGU facility in address table
        hub = address_lookup[0]

        # Extract delivery addresses for package
        addresses = self.get_addresses()

        # Calculate delivery route
        route = routing.get_route(hub, addresses, address_lookup, distance_lookup)

        # Calculate distance of delivery route
        route_distance = routing.get_route_distance(route, address_lookup, distance_lookup)

        # Calculate time to complete route
        time_to_complete = route_distance / self.speed

        # Specify return time for 'time' based calculations
        self.return_time = self.departure_time + time_to_complete

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

            # calculate time it takes to drive distance required
            time_to_address = delivery_distance / self.speed

            # using time calculated, set package delivery time to departure time + time taken to deliver
            for p in self.packages:
                # lookup packages based on address
                if p.address == address:
                    p.delivery_time = self.departure_time + time_to_address
                    # once delivered, remove package from truck
                    self.packages.remove(p)
