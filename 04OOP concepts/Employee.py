class Employee:
    empCount = 0
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
        
    def display(self):
        print("ID of employee is "+self.id)
        print("Name of employee is "+self.name)
    
    
emp1 = Employee("Sandesh", "1")
    
emp1.display()