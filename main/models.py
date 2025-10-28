from django.db import models
from django.contrib.auth.models import User

# One-to-One (User Profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username

# One-to-Many (Restaurant → FoodItems)
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='foods/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

# Many-to-Many (Customer ↔ FoodItem through Order)
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
# Create your models here.
