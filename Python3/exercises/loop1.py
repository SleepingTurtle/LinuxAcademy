user = { 'admin': False, 'active': True, 'name': 'Kevin' }

if user['admin'] == True & user['active'] == True:
    print('ACTIVE - (ADMIN) - user')
elif user['admin'] == True:
    print('(ADMIN) - user')
elif user['active'] == True:
    print ('ACTIVE - user')
else:
    print('user')
