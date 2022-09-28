
from cProfile import label
from this import s
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group

from adhoc_mobile.constants import ACTIVE_CHOICES

class TimestampModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Creation Date/Time',auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Update Date/Time', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class Project(TimestampModel):
    name = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name


class Employee(TimestampModel):

    # define relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    # define fields
    job_options = (('1', 'data collector'), ('2', 'merchandiser'),
                   ('3', 'back office'), ('4', 'supervisor'), ('5', 'admin'))
    identifier = models.CharField(max_length=20)
    name = models.CharField(max_length=50, null=True, unique=True)
    isDisabled = models.BooleanField(default=False)
    profilePicture = models.ImageField(
        upload_to='profile_pictures/', blank=True)
    phone = models.CharField(max_length=11)
    forceOnlineConnectivity = models.BooleanField(default=False)
    job_option = models.CharField(max_length=50, choices=job_options)
    

@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.employee.save()



class Country(TimestampModel):
    name = models.CharField(max_length=50, unique=True, null=True)
    
    def __str__(self):
        return self.name



class City(TimestampModel):
    name = models.CharField(max_length=50, unique=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    


class Area(TimestampModel):
    name = models.CharField(max_length=50, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    


class Region(TimestampModel):
    name = models.CharField(max_length=50, unique=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Plan(TimestampModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    force_sequence = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)


class Rule(TimestampModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, null=True, to_field='name')

    rule_types = (
        ('weekly', 'weekly'), ('daily', 'daily'), ('monthly', 'monthly'))
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=rule_types)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    occurrences = models.IntegerField()
    note = models.CharField(max_length=50)
    force_sequence = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)

#  route model


class Route(TimestampModel):
    project = models.ManyToManyField(Project)
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    force_sequence = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)







class Client(TimestampModel):
    # define relations here
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, to_field='name', null=True)
    route = models.ManyToManyField(Route)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    # define fields here
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=200)
    client_code = models.CharField(max_length=9)
    formatted_address = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_title = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    chain = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    payment_terms = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50, default='cash', choices=(
        ('cash', 'cash'), ('credit', 'credit')))
    geofencing_radius = models.FloatField()
    credit_limit = models.FloatField()
    status = models.CharField(max_length=50)
    latest_visit = models.DateTimeField()
    comment = models.TextField(max_length=200, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', blank=True)
    logo = models.ImageField(upload_to='logos', blank=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    is_disabled = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    is_chain = models.BooleanField(default=False)
# visit model
class Visit(TimestampModel):
    # define relations here
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    route = models.ManyToManyField(Route)

    # define fields here
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_duration = models.TimeField()

    store_location = models.CharField(max_length=50)
    end_location = models.CharField(max_length=50)

    distance = models.FloatField()
    start_distance = models.CharField(max_length=50)
    end_distance = models.CharField(max_length=50)
    delta_distance = models.FloatField()
    start_in_geofence = models.BooleanField(default=False)
    end_in_geofence = models.BooleanField(default=False)
    auto_closed_by_geofence = models.BooleanField(default=False)

# audit model


class Audit(TimestampModel):
    # define relations here
    visit = models.OneToOneField(Visit, on_delete=models.CASCADE)

    # define fields here
    shelf_quantity = models.IntegerField()
    shelf_price = models.DecimalField(decimal_places=2, max_digits=10)
    store_quantity = models.IntegerField()
    note = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='inventoryImages', blank=True)
# category model




class Product(TimestampModel):
    # define relations
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    category_name = models.CharField(max_length=100, null=True)
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, null=True)
    # client = models.ManyToManyField(Client)

    # define fields
    name = models.CharField(max_length=200, unique=True, null=True)
    local_name = models.CharField(max_length=200)
    sku = models.CharField(max_length=10)
    barcode = models.CharField(max_length=50)
    description = models.TextField()
    retailSelling_price = models.DecimalField(max_digits=12, decimal_places=2)
    brand = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=4, decimal_places=2 ,blank=True)
    measure_unit = models.CharField(max_length=50)
    auditable = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    frozen_preSale = models.BooleanField(default=False)
    frozen_sale = models.BooleanField(default=False)
    exp_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='products/', blank=True,max_length=500)

class Image(TimestampModel):
    image_types = (('1' , 'before') ,('2', 'after'), ('3', 'regular'))
    name = models.CharField(max_length=50)
    image_type = models.CharField(max_length=50 , choices=image_types , default='3')
    photo = models.ImageField(upload_to='stores/', blank=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name 



class Field(models.Model):
    choices=(
        ('text', 'text'),
        ('button','button'),
         ('color', 'color'),
           ('number', 'number'),
        ('password','password'),
         ('radio', 'radio'),
        ('date','date'),
         ('search','search'),
         ('datetime-local', 'datetime-local'),
        ('email','email'),
         ('file', 'file'),
        ('hidden','hidden'),
         ('image', 'image'),
        ('month','month'),
    )
    label = models.CharField(max_length= 10000)
    field_type = models.CharField(max_length=20,default='text', choices=choices)
    required = models.BooleanField(default=False)


class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Field, on_delete = models.CASCADE ,related_name = "answer_to")

class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    field = models.ManyToManyField(Field, related_name = "fields")

# add tokens to new users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)






