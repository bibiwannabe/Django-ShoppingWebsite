from django.shortcuts import render
from shopping_user.models import UserInfo
def order(request):
    uid = request.session['user_id']
    user= UserInfo.objects.get(pk=int(uid))
    context = {
        'user_order':1,
        'page_name':1,
        'user':user
    }
    return render(request,'user_order/place_order.html',context)
# Create your views here.
