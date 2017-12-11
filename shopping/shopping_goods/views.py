from django.shortcuts import render
def index(request):

    return render(request,'shopping_goods/index.html')

def list(request):
    return render(request,'shopping_goods/list.html')

def detail(request):
    return render(request, 'shopping_goods/detail.html')
# Create your views here.
