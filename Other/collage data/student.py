class Student:
    
    def read_info(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.department = input("Enter department: ")
        self.mobile_no = input("Enter mobile number: ")

    def print_info(self):
        print("Student Information:")
        print("Name:", self.name)
        print("Roll No.:", self.roll_no)
        print("Department:", self.department)
        print("Mobile No.:", self.mobile_no)


student1 = Student()

student1.read_info()

student1.print_info()
