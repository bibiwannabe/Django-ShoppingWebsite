from django.shortcuts import render
def order(request):
    context = {
        'user_order':1,
        'page_name':1,
    }
    return render(request,'user_order/place_order.html',context)
# Create your views here.
