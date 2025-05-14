# Implement a package class to easily store package information for convenient retrieval
class Package:
    def __init__(self, id, address, deadline, city, zipcode, weight, delivery_status = "At Hub" ):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.delivery_status = delivery_status

    # Implement a representation of a package that displays all stored info at once
    def __repr__(self):
        return f"""
        Package ID: {self.id}
        Address: {self.address}
        Deadline: {self.deadline}
        City: {self.city}
        Zip Code: {self.zipcode}
        Weight: {self.weight}
        Delivery Status: {self.delivery_status}
        """

    # Getter functions used to return individual package information
    def get_id(self):
        return self.id

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

    def get_delivery(self):
        return self.delivery_status

    # Setter functions used to update package information, if necessary.
    # NOTE: set_id not given, because id would be primary key in database
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

    def set_delivery(self, delivery):
        self.delivery = delivery
