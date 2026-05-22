# #Single level inheritance
# class College:
#     def College_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name:  Prashant Jha")
#         print("Branch: Merchanical")

# # obj = Student()
# # obj.College_name()
# # obj.student_info()

# class Exam(Student):
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Student3: C-Language")

# obj = Exam()
# obj.College_name()
# obj.student_info()
# obj.subject()




#Multiple inheritance
# class Subjmarks:
#     def __init__(self):
#         # Moving inputs inside __init__ makes them proper object attributes
#         self.math = int(input("Enter paper marks of math : "))
#         self.DE = int(input("Enter paper marks of design engineering : "))
#         self.C = int(input("Enter paper marks of c language : "))
#         self.english = int(input("Enter paper marks of english : "))

# class PractMarks:
#     def __init__(self):
#         self.cpract = int(input("Enter practicals marks of c language : "))

# # Fixed the typos: matching 'Subjmarks' and 'PractMarks' exactly
# class Result(Subjmarks, PractMarks):
#     def __init__(self):
#         # Initialize both parent classes properly
#         Subjmarks.__init__(self)
#         PractMarks.__init__(self)

#     def total(self):
#         # Fixed 'self.c' to match 'self.C' (case sensitivity mattering again!)
#         if (self.math >= 40 and 
#             self.DE >= 40 and 
#             self.C >= 40 and 
#             self.english >= 40 and 
#             self.cpract >= 20):
#             print("Result: PASS")
#         else:
#             print("Result: FAIL")

# # Now, running this line will trigger the inputs properly
# obj = Result()
# obj.total()





class Rb1:
    def home_loan(self):
        print("Home Loan ROI = 8%")

    def education_loan(self):
        print("Education loan = 9%")

class Sb1:
    def education_loan(self):
        print("Education loan = 10%")

obj = Sb1()
obj.education_loan()
