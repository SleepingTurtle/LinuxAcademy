#!/usr/bin/env python3.6

users = [
        { 'admin': False, 'active': True, 'name': 'Kevin' },
        { 'admin': True, 'active': False, 'name': 'Bob' },
        { 'admin': True, 'active': True, 'name': 'Dog' },
        { 'admin': False, 'active': False, 'name': 'You' }
]
prefix = ""
line_num = 1

for user in users:
    if user['admin'] and user['active']:
            prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
            prefix = "(ADMIN) "
    elif user['active']:
            prefix = "ACTIVE - "

    print(str(line_num) + ": " + prefix + user['name'])
    line_num += 1
    prefix = ""
