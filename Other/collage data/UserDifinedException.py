class AgeException(Exception):
    pass


while True:

    age = int(input("Enter the age of user : "))
    try:
        if age <= 18:
            raise AgeException("Invalid age...!")
        else:
            print('You can voat..!')
        
    except AgeException as e:
        print(e)

