class School:
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_Town = school_Town

    def get_school_info(self):
        return f"School Name: {self.school_name}, Address: {self.school_Town}"
