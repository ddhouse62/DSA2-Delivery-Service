# Implement a package class to easily store package information for convenient retrieval
class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, weight, delivery_status = "At Hub" ):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.delivery_status = delivery_status
        self.arrival_time = None
        self.departure_time = None
        self.delivery_time = None

    # Implement a representation of a package that displays all stored info at once
    def __repr__(self):
        return f"""
        Package ID: {self.package_id}
        Address: {self.address}
        City: {self.city}
        Zip Code: {self.zipcode}
        Deadline: {self.deadline}
        Weight: {self.weight}
        Delivery Status: {self.delivery_status}
        """

    # Getter functions used to return individual package information
    def get_package_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def get_deadline(self):
        return self.deadline

    def get_city(self):
        return self.city

    def get_zipcode(self):
        return self.zipcode

    def get_weight(self):
        return self.weight

    def get_delivery_status(self):
        return self.delivery_status

    # Setter functions used to update package information, if necessary.
    # NOTE: set_package_id not given, because package_id would be primary key in database
    def set_address(self, address):
        self.address = address

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_city(self, city):
        self.city = city

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def set_weight(self, weight):
        self.weight = weight

    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status

    # package method designed to assist with readability.  Returns packages by ID if address matches current address
    def address_to_package(self, address):
        if address == self.address:
            return self.package_id

    # method to easily return the delivery address of a given package given its ID
    def package_to_address(self, package_id):
        return self.address
