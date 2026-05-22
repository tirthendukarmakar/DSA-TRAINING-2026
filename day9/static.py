class Student:
    @staticmethod
    def get_personal_detail(firstname,lastname):
        print("your personal detail=",firstname,lastname)

    @staticmethod
    def contact_detail(mobil_no,rollno):
        print("your contact details=",mobil_no,rollno)

Student.get_personal_detail("prashant","jha")
Student.contact_detail(5456454646,1001)