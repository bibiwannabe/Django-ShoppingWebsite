# coding='utf-8'
from django.shortcuts import render
from . import models
from .models import TypeInfo,GoodsInfo
from django.core.paginator import  Paginator, Page

def index(request):
    typelist = models.TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type00 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type02 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type03 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type04 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type05 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context={'type0': type0, 'type00': type00,
             'type1': type1, 'type01': type01,
             'type2': type2, 'type02': type02,
             'type3': type3, 'type03': type03,
             'type4': type4, 'type04': type04,
             'type5': type5, 'type05': type05,
             'page_name':1}

    return render(request,'shopping_goods/index.html',context)



def list(request,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort =='1':
        goods_list = GoodsInfo.objects.filter(gtype_id = int(tid)).order_by('-id')
    elif sort =='2':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort =='3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list, 10)
    print(paginator)
    page = paginator.page(int(pindex))
    context={
        'tid':tid,
        'page': page,
        'pahinator': paginator,
        'typeninfo': typeinfo,
        'sort': sort,
        'news': news,
        'list':1
    }

    return render(request,'shopping_goods/list.html',context)

def detail(request,gid):
    good = GoodsInfo.objects.get(pk=int(gid))
    good.gclick =good.gclick+1
    good.save()
    news = good.gtype.goodsinfo_set.order_by('-id')[0:2]
    context ={
        'good':good,
        'news':news,
        'gid':gid,
        'list':1
    }
    #记录最近浏览
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_id ='%d'%good.id#变成字符串
    if goods_ids!='':
        goods_ids1=goods_ids.split(',')
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>=6:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids=goods_id
    request.set_cookie('goods_ids',goods_ids)

    return render(request, 'shopping_goods/detail.html',context)

def cart(request):
    context = {
        'guest_cart':1
    }
    return render(request,'user_cart/cart.html',context)
# Create your views here.
