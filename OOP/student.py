class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Course: {self.course}, Index number: {self.index_number}"


student1 = Student("John Benson", "High Park 36", "(507) 833-3567", "Geography", "123/007")
student2 = Student("Alice Johnson", "Green Street 24", "(508) 555-1234", "History", "456/009")
student3 = Student("Bob Smith", "Oak Avenue 15", "(509) 777-9876", "Mathematics", "789/003")


print(student1.getInfo())
print(student2.getInfo())
print(student3.getInfo())
