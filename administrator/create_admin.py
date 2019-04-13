from django.contrib.auth.models import User
from . models import Admin
from . choice import DEPARTMENT_CHOICES

username = input("Enter user name:")
password = input("Enter admin password: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter emailID: ")
print(DEPARTMENT_CHOICES)
brach = input("Enter branch code: ")


user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name, email=email, is_staff=True)
admin = Admin.objects.create(user=user, branch=brach)

print("Admin created")