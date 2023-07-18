from django.contrib.auth.models import User
from django.db import models
#
# # Create your models here.
# class Acadamic_year(models.Model):
#     title=models.CharField(max_length=255)
#     year_from=models.IntegerField()
#     year_to=models.IntegerField()
#
# class Term(models.Model):
#     Term_Acadamic_year=models.ForeignKey(Acadamic_year,on_delete=models.CASCADE)
#     name=models.CharField(max_length=255)
#     types= (
#         ('Even', 'Even'),
#         ('Odd', 'odd '),
#         # (),
#     )
#     type = models.CharField(max_length=10, choices=types)
#     start_date=models.DateField()
#     end_date=models.DateField()
#     status_enum=(
#         ('current','current'),
#         ('completed','completed'),
#     )
#     status=models.CharField(max_length=100,choices=status_enum)
#
# # class stream(models.Model):
# #     stream_name=models.CharField(max_length=255)
#
#
#
#
# class qualification(models.Model):
#     qualification_Name=models.CharField(max_length=255)
#     stream_enum=(
#         ('engineering','engineering'),
#         ('Sciene','Sciene'),
#         ('Commerce','Commerce'),
#         ('Arts','Arts'),
#         ('Diploma','Diploma')
#     )
#     Stream = models.CharField(max_length=100, choices=stream_enum)
#     qualification_Level=(
#         ('UG','UG'),
#         ('PG','PG'),
#         ('Diploma',"Diploma"),
#         ('PHD','PHD'),
#         ('Secondary_Schoolin','Secondary_Schoolin'),
#     )
#     specilization=models.CharField(max_length=100)
#
# class caste(models.Model):
#     state_id=models.IntegerField()
#     state_name=models.CharField(max_length=100)
#     caste_code=models.IntegerField()
#     Caste_name=models.CharField(max_length=100)
#     subcaste=models.CharField(max_length=125)
#
# class Designation(models.Model):
#     Designation_Full_Name=models.CharField(max_length=255)
#     acronym=models.CharField(max_length=6)
#     Description=models.TextField(max_length=480)
#
# class Address(models.Model):
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country=models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=10)
#
# class AddressType(models.Model):
#     Address=models.ForeignKey(Address,on_delete=models.CASCADE)
#     ad_type_enum=(
#         ('Permanent','Permanent'),
#         ('Communicational','Communicational'),
#         ('Residential','Residential'),
#     )
#
#     ad_type=models.TextField(max_length=1000 ,choices=ad_type_enum)
#

class stream(models.Model):
    name=models.CharField(max_length=250)
    acronym = models.CharField(max_length=10)
    description=models.TextField()
    status=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    updated_on=models.DateTimeField(auto_now=True)


class specialization(models.Model):
    name=models.CharField(max_length=150)
    acronym=models.CharField(max_length=10)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class level(models.Model):
    name=models.CharField(max_length=150)
    acronym=models.CharField(max_length=10)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class Qualifications(models.Model):
    name=models.CharField(max_length=150)
    acronym = models.CharField(max_length=10)
    # description = models.TextField()
    stream=models.ForeignKey(stream,on_delete=models.CASCADE)
    level=models.ForeignKey(level,on_delete=models.CASCADE)
    specialization=models.ForeignKey(specialization,on_delete=models.CASCADE)
    status = models.IntegerField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

class Country(models.Model):
    name=models.CharField(max_length=150)
    acronym=models.CharField(max_length=12)
    country_code=models.CharField(max_length=10)
    status = models.IntegerField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class State(models.Model):
    name=models.CharField(max_length=150)
    acronym=models.CharField(max_length=15)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    status = models.IntegerField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class Dist(models.Model):
    name=models.CharField(max_length=150)
    acronym = models.CharField(max_length=12)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    status = models.IntegerField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class Talluk(models.Model):
    name=models.CharField(max_length=150)
    acronym = models.CharField(max_length=12)
    dist=models.ForeignKey(Dist,on_delete=models.CASCADE)
    status = models.IntegerField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class City(models.Model):
    name=models.CharField(max_length=150)
    acronym = models.CharField(max_length=12)
    talluk=models.ForeignKey(Talluk,on_delete=models.CASCADE)
    dist=models.ForeignKey(Dist,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class Pincode(models.Model):
    pincode=models.IntegerField()
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class medium(models.Model):
    name=models.CharField(max_length=120)
    acronym = models.CharField(max_length=12)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class Languge(models.Model):
    name=models.CharField(max_length=150)
    acronym = models.CharField(max_length=12)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

    # Caste related table................

class Religion(models.Model):
    religion_code = models.CharField(max_length=30)
    religion_name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class Caste(models.Model):
    caste_code = models.CharField(max_length=30)
    caste_name = models.CharField(max_length=30)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class Subcaste(models.Model):
    subcaste_code = models.CharField(max_length=30)
    subcaste_name = models.CharField(max_length=30)
    caste = models.ForeignKey(Caste, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

class Designation(models.Model):
    name = models.CharField(max_length=120)
    acronym = models.CharField(max_length=12)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class Committe(models.Model):
    name=models.CharField(max_length=350)
    acronym=models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
class FeeCategory(models.Model):
    FEE_TYPE_CHOICES = (
        ('Mandatory', 'Mandatory'),
        ('Recursive', 'Recursive'),
        ('Optional', 'Optional'),
    )

    name = models.CharField(max_length=255)
    fee_type = models.CharField(max_length=250, choices=FEE_TYPE_CHOICES)
    acronym = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)



class EntryType(models.Model):
    name=models.CharField(max_length=250)
    acronym = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

