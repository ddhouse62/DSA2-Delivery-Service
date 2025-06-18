import datetime

# Implement a package class to easily store package information for convenient retrieval
class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.arrival_time = None
        self.departure_time = None
        self.delivery_time = None
        if package_id in [6, 25, 28, 32]:
            self.arrival_time = datetime.time(9,5)
        else:
            self.arrival_time = datetime.time(8,0)


    # Implement a representation of a package that displays all stored info at once
    def __repr__(self):
        return f"""
        Package ID: {self.package_id}
        Address: {self.address}
        City: {self.city}
        Zip Code: {self.zipcode}
        Deadline: {self.deadline}
        Weight: {self.weight}
        Delivery Time: {self.delivery_time}
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

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    # Function to dynamically get delivery status based on a given time
    # Defaults to end of day, but optional 'time' component allows for
    def get_delivery_status(self, time):
            if time < self.arrival_time and time < datetime.time(8,0,0):
                self.delivery_status = "Not yet arrived at hub"
            elif time < self.arrival_time:
                self.delivery_status = "Delayed"
            elif time >= self.arrival_time and time < self.departure_time:
                self.delivery_status = "At Hub"
            elif time >= self.departure_time and time < self.delivery_time:
                self.delivery_status = "En Route"
            else:
                self.delivery_status = f"Delivered at {self.delivery_time.strftime("%I:%M:%S %p")}"
            return self.delivery_status


    # Provides a representation of package based on given time for lookup function
    def get_package_stats(self, time):
        if self.get_package_id() == 9 and time < datetime.time(10,20,0):
            return f"""
            Package ID: {self.package_id}
            Address: 300 State St
            City: Salt Lake City
            Zip Code: 84103
            Deadline: {self.deadline}
            Weight: {self.weight}
            Delivery Status at {time.strftime("%I:%M:%S %p")}: {self.get_delivery_status(time)}
            """
        else:
            return f"""
            Package ID: {self.package_id}
            Address: {self.address}
            City: {self.city}
            Zip Code: {self.zipcode}
            Deadline: {self.deadline}
            Weight: {self.weight}
            Delivery Status at {time.strftime("%I:%M:%S %p")}: {self.get_delivery_status(time)}
            """
