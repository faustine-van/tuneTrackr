#!/usr/bin/env python3
"""1-main module"""
from models.user import User, Role, UserRole
from models import dbStorage

# Create a new user instance
# user = User(email="barbie@gmail.com", password="12345")
# role = Role(name="Standard")
# role.save()
users = dbStorage.search(User, {"email": "selena@gmail.com"}).values()
users_json = [user.to_json() for user in users]
print(users_json[0]['id'])
user_role = UserRole(user_id=users_json[0]['id'], role_id="c8a491d2-292e-44ef-a043-a76feff42cff")
user_role.save()
# roles = dbStorage.search(Role, {"name": "Standard"}).values()

# for user, role in zip(users, roles):
#    print(user.id, role.id)
#    user_role = UserRole(user_id=user.id, role_id=role.id)
#    user_role.save()


# add role
# roles = ["Admin", "Analyst", "Manager", 'Artist']
# for role in roles:
#    role = Role(name=role)
#    role.save()
