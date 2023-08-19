#  Regirstation Form

name = input('Enter the name : ')
user_id  = input('Enter the user id : ')
phonNumber = input('Enter the phone number : ')
if(name.isalpha()):
    print('Name send successful')
    if(user_id.isalnum()):
        print('User name send successful')
        if(phonNumber.isnumeric()):
            print('Number send successful')

print(name.isdigit())