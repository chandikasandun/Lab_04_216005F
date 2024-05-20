class Address:
    def _init_(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

     def _str_(self):
        return f"{self.street}, {self.city}, {self.zipcode}"
