from django.db import models

# Create your models here.
##COMMON##

class Country(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=5, null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=5, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state_country')
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='city_state')
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name


##USERS##
class CustomUser(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100,unique=True, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=True)

class User(models.Model):
    name = models.CharField(max_length=100,)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_username')
    email = models.EmailField(max_length=100,unique=True,)
    phone = models.CharField(max_length=15, )
    address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='user_city')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='user_state')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country')
    zip = models.CharField(max_length=10, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_updated_by')
    def __str__(self):
        return self.username
