Username = 'mahya'
Pass = '751275'
count = 0

for i in range (3):
    user = input('Enter your user: ')
    password = input('Enter your password: ')
    if (user == Username) and (password == pass):
        print('welcome!')
        break
    elif (user != Username) or (password != Pass):
        if (count == 2):
            print('Your account has been locked :(')
            break
        print('Your user or password is incorrect. Please try again!')

    count = count + 1
