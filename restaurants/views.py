from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants_list.html', {'restaurants': restaurant})

