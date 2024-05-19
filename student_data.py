from student import Student
from school import School
from parent import Parent

# Example usage
if __name__ == "__main__":
    # Creating a student instance
    student1 = Student("A.M.C.S.Arachchi", "216005F")
    student2 = Student("P.S.G. Dabare", "216019C")

    # Creating a school instance
    school1 = School("Central College Anuradhapura", "Anuradhapura")
    school2 = School("Viharamahadevi Balika Vidyalaya, "Gampaha")

    # Creating a parent instance
    parent1 = Parent(student1, "Sunil Gamini", "0772893387")
    Parent2 = Parent(student2, "Deshapriya Dabare", "0776458392")

    # Printing information
    print(student1.get_student_info())
    print(school1.get_school_info())
    print(parent1.get_parent_info())
    print(student2.get_student_info())
