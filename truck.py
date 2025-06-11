# implement a truck class to carry packages for delivery

# Capacity and speed are both constants and are not modified, will not be accessible by user by default
CAPACITY = 16
SPEED = 18

class Truck:
    def __init__(self, id, packages, mileage = 0, status = "At Hub"):
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

        self.speed = SPEED

        self.status = "At Hub"


    # Method to quickly load trucks with pre-defined lists of packages
    def load(self, packages_to_load):
        if len(self.packages) + len(packages_to_load) <= self.capacity:
            for package in packages_to_load:
                package.set_delivery = "En Route"
                self.packages.append(package)
        else:
            raise ValueError(f"Packages on Truck cannot exceed {self.capacity}.\nCurrent Load: {len(self.packages)}.\nNumber of packages loaded: {len(packages_to_load)}.")

    def get_addresses(self):
        addresses = []
        for p in self.packages:
            addresses.append(p.address)
        return addresses
