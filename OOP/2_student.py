class Student:
    def __init__(self,name,age,academy,year):
        self.name = name
        self.age = age
        self.academy = academy
        self.year = year
    
    def passed_exams(self):
        print("Student with name "+self.name+" passed the exams successfully")
    def failed_exams(self):
        print("Student with name "+self.name+" failed the exams!")


student_1 = Student("Mikey",16,"Oxford",2024)
student_2 = Student("Draken",18,"Harvard",2024)


student_1.passed_exams()
student_2.failed_exams()