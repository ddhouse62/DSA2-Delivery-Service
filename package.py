class Package:
    def __init__(self, id, address, deadline, city, zipcode, weight, delivery_status = "At Hub" ):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.delivery_status = delivery_status
