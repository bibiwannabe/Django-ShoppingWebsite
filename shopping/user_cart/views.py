from django.shortcuts import render

def cart_order(request):
    context={
        'cart':1,
    }
    return render(request, 'user_cart/place_order.html')
# Create your views here.
