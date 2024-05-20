from student import Student
from school import School
from parent import Parent

# Example usage
if __name__ == "__main__":
    # Creating a student instance
    student1 = Student("A.M.C.S.Arachchi", "216005F")
    student2 = Student("P.S.G. Dabare", "216019C")
    student3 = Student("K.P.H.S Karunathilake", "216063E")
    

    # Creating a school instance
    school1 = School("Central College Anuradhapura", "Anuradhapura")
    school2 = School("Viharamahadevi Balika Vidyalaya", "Gampaha")
    school3 = School("Musaeus College", "Colombo")

    # Creating a parent instance
    parent1 = Parent(student1, "Sunil Gamini", "0772893387")
    Parent2 = Parent(student2, "Deshapriya Dabare", "0776458392")
    parent2 = Parent(student3, "Gamini Karunathilake", "0714567245")

    # Create instances of Address
    address1 = address(student1, "562/D6,Jayanthi Mawatha","Anuradhapura","50000")
    address2 = address(student2, "356/1,Radawana", "Gampaha", "11254")
    address3 = address(student3, "180/A,Main Raod", "Nawagamuwa", "10654")

                       
    # Printing information
    print(student1.get_student_info())
    print(school1.get_school_info())
    print(parent1.get_parent_info())
    print(student2.get_student_info())
    print(address1.get_student_info())
    print(student3.get_student_info())
