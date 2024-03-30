#!/usr/bin/python3
"""main.file"""
from models.user import User
from models import dbStorage

# Create a new user instance
user = User(email="bibo.com", password="12345")
# user1 = User(email='bruno@gmail.com', password='12345')

# Save the user to the database
user.save()
# user1.save()

# Print the user data as JSON
# for user in dbStorage.all().values():
#    print(user.to_json())

# search data
for data in dbStorage.search(User, {"password": "12345"}).values():
    print(data.to_json())

# updated
# id = '3f4bc01a-3dd0-4a93-8715-1ab18ec55e08'
# user3 = dbStorage.get(User, id)
# print(user.to_json())

# user3.email = 'blue@gmail.com'
# dbStorage.save()

# count
# count = dbStorage.count()
# print(count)

# delete obj
# for del_user in dbStorage.search({sour'email': 'kali'}).values():
#    dbStorage.remove(del_user)
# dbStorage.save()

# validate password
# id = 'c9aa775a-de1b-45ce-8779-c9ba3ca9f95c'
# user3 = dbStorage.get(User, id)
# if user3.is_validpassword('12345') is True:
#    print('valid password')
# else:
#    print('no valid password')
