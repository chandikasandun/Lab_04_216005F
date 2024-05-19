class Student:
    def __init__(self, name, index_number):
        self.name = name
        self.index_number = index_number

    def get_student_info(self):
        return f"Student Name: {self.name}, Index Number: {self.index_number}"