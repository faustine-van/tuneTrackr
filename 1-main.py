#!/usr/bin/python3
"""1-main module"""
from models.user import User, Role, UserRole
from models import dbStorage

# Create a new user instance
user = User(email="barbie@gmail.com", password="12345")
role = Role(name="Standard")
# role.save()
users = dbStorage.search(User, {"email": "barbie@gmail.com"}).values()

roles = dbStorage.search(Role, {"name": "Standard"}).values()

for user, role in zip(users, roles):
    print(user.id, role.id)
    user_role = UserRole(user_id=user.id, role_id=role.id)
    user_role.save()


# count
count = dbStorage.count(Role)
print(count)
