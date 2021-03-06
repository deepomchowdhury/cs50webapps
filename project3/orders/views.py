from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

from .models import Menu, MenuItem, Topping, OrderItem, Order, Variation, Pizza

from .forms import SignUpForm

import json

# Create your views here.

# signup view
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'orders/signup.html'

# index page
def index(request):

    context = {
        'menus':  Menu.objects.all(),
    }
    return render(request, 'orders/index.html', context)

# cart page
@login_required
def cart(request):

    return render(request, 'orders/cart.html')

# display orders placed
@user_passes_test(lambda u: u.is_superuser)
def display_orders(request):

    context = {
        'orders': Order.objects.filter(status='not completed')
    }
    return render(request, 'orders/display_orders.html', context)

# display orders placed
@login_required
def orders_history(request):

    context = {
        'orders': Order.objects.filter(user=request.user)
    }
    return render(request, 'orders/history.html', context)

# order api
@login_required
def order(request):

    if request.method == 'POST':
        order = json.loads(request.body)
        menu_item = MenuItem.objects.get(pk=int(order['id']))

        if order['variation'] != '':
            variation = menu_item.variations.get(name=order['variation'])
            order_price = variation.price * int(order['quantity'])
        else:
            order_price = menu_item.price * int(order['quantity'])

        description = f"{menu_item.name}  {order['variation']},"
        if len(order['toppings']) > 0:
            description +=  " toppings: "
            for topping in order['toppings']:
                description += topping['name'] + ", "

        order_obj = Order.objects.create(
            user = request.user,
            price = round(order_price, 2),
            description = description,
            quantity = int(order['quantity'])
        )
        
        order_item = OrderItem.objects.create(
            name = menu_item.name,
            category = menu_item.category,
            veg = menu_item.veg,
            price = menu_item.price,
            order = order_obj
        )

        if order['variation'] != '':
            Variation.objects.create(
                name = variation.name,
                price = variation.price,
                order_item = order_item
            )

        if len(order['toppings']) > 0:
            pizza = Pizza.objects.create(
                order_item = order_item,
                num_of_toppings = len(order['toppings'])
            )
            for topping in order['toppings']:
                Topping.objects.get(name=topping['name']).pizza.add(pizza)
    
        return JsonResponse(
            {
                'order': {
                    'user': order_obj.user.username,
                    'price': order_obj.price,
                    'quantity': order_obj.quantity
                }
            }
        )

# update status
@user_passes_test(lambda u: u.is_superuser)
def update_order(request):

    if request.method == 'POST':
        order = json.loads(request.body)
        Order.objects.filter(pk=int(order['id'])).update(status=order['status'])

        return JsonResponse(order)

# menu items api
def item_api(request, item_id):

    try:    
        item = MenuItem.objects.get(pk=item_id)
    except:
        return HttpResponse(status=500)

    variations = []
    features = []
    
    for variation in item.variations.all():
        variations.append({'name':variation.name, 'price':variation.price})

    try:
        if item.pizza:
            features.append({'num_of_toppings':item.pizza.num_of_toppings})
    except:
        pass

    return JsonResponse(
        {
            'id': item.id,
            'name': item.name,
            'img': item.img,
            'price': item.price,
            'veg': item.veg,
            'variations': variations,
            'more_features': features
        },
        safe=False
    )

# get toppings
def toppings_api(request):
        
    toppings = []

    for topping in Topping.objects.all():
        toppings.append({'name': topping.name})

    return JsonResponse(
        {
            'toppings': toppings
        },
        safe=False
    )

# get menus
def menus_api(request):

    menus = []

    for menu in Menu.objects.all():
        items = []
        
        for item in menu.menu_items.all():
            
            variations = []
            
            for variation in item.variations.all(): 
                variations.append({'name':variation.name, 'price':variation.price})
            
            items.append({'id':item.id, 'name':item.name, 'img':item.img, 'description':item.description, 'variations':variations})
        
        menus.append({
            'name': menu.name,
            'items': items,
        })
    
    return JsonResponse(
        {
            'menus': menus
        },
        safe=False
    )

# logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')