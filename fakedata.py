import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserDataAuth.settings')

import django
django.setup()

from faker import Faker
faker=Faker()
from datetime import date
from testapp.models import UserDetails



def fakedata(n):
    for i in range(n):
        name=faker.name()
        birth_date = faker.date_of_birth(minimum_age=18, maximum_age=90)
        today = date.today()
        age = int(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        role=faker.job()
        address=faker.city()
        UserDetails.objects.get_or_create(
            name=name,
            age=age,
            role=role,
            address=address
        )
n=int(input("Enter no.of users to enter:"))
fakedata(n)