class Employee:
    id = None
    name = None

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def displayData(self):
        print("Id of employee : ",self.id)
        print("Name of employee : ",self.name)


ob = Employee(1,'Sandesh')
ob.displayData()