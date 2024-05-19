from student import Student

class Parent:
    def __init__(self, student, parent_name, contact_number):
        self.student = student
        self.parent_name = parent_name
        self.contact_number = contact_number

    def get_parent_info(self):
        return f"Parent Name: {self.parent_name}, Contact Number: {self.contact_number}, Student: {self.student.get_student_info()}"
