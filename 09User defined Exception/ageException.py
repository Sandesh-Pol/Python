class InvalideAgeException(Exception):
    pass

while True:
    age_input = input("Enter your age: ")

    try:
        age = int(age_input)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        if age > 18:
            print("You can vote.")
        else:
            raise InvalideAgeException("You cannot vote.")
        continue

    except ValueError:
        print("Invalid input. Please enter a valid age (a positive integer).")

    except InvalideAgeException as e:
        print(e)  
