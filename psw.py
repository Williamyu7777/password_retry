# password = a123456
i = 3
while i <= 3 and i > 0:
    password = input('please input password:')   
    if password == 'a123456':
        print('logged in success!')
        break
    else:
        print('wrong password you still have', i-1, 'times')
        i = i-1
