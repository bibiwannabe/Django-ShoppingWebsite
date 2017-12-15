# coding=utf-8
# -*- coding: utf-8 -*-
from datetime import datetime
from decimal import Decimal

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from shopping_user.models import UserInfo
from shopping_user.user_decorator import login
from user_cart.models import CartInfo
from shopping_goods.models import GoodsInfo
from .models import OrderInfo,OrderDetailInfo

@login
def order(request):
    uid = request.session['user_id']
    user= UserInfo.objects.get(pk=int(uid))
    orderid = request.GET.getlist('orderid')
    orderlist = []
    for id in orderid:
        orderlist.append(CartInfo.objects.get(id=int(id)))

    # 判断用户手机号是否为空，分别做展示
    if user.userphone == '':
        userphone = ''
    else:
        userphone = user.userphone[0:4] + \
            '****' + user.userphone[-4:]
    context = {
        'title':'提交订单',
        'user_order':1,
        'page_name':1,
        'user':user,
        'orderlist':orderlist,
        'userphone':userphone
    }
    return render(request,'user_order/place_order.html',context)

@transaction.atomic()
@login
def order_handle(request):
    #保存一个事物点
    tran_id = transaction.savepoint()
    #接收购物车编号
    # 根据POST和session获取信息
    # cart_ids=post.get('cart_ids')
    try:
        post = request.POST
        orderlist = post.getlist('id[]')
        total = post.get('total')
        address = post.get('address')

        order=OrderInfo()
        now=datetime.now()
        uid = request.session.get('user_id')
        order.oid='%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id=uid
        order.odate=now
        order.ototal=Decimal(total)
        order.oadd = address
        order.save()

        # 遍历购物车中提交信息，创建订单详情表
        for orderid in orderlist:
            cartinfo = CartInfo.objects.get(id=orderid)
            good = GoodsInfo.objects.get(cartinfo__id=cartinfo.id)

            # 判断库存是否够
            if int(good.gstock) >= int(cartinfo.count):
                # 库存够，移除购买数量并保存
                good.gstock -= int(cartinfo.count)
                good.save()

                goodinfo = GoodsInfo.objects.get(cartinfo__id=orderid)

                # 创建订单详情表
                detailinfo = OrderDetailInfo()
                detailinfo.goods_id = int(goodinfo.id)
                detailinfo.order_id = int(order.oid)
                detailinfo.price = Decimal(int(goodinfo.gprice))
                detailinfo.count = int(cartinfo.count)
                detailinfo.save()

                # 循环删除购物车对象
                cartinfo.delete()
            else:
                # 库存不够出发事务回滚
                transaction.savepoint_rollback(tran_id)
                # 返回json供前台提示失败
                return JsonResponse({'status': 2})
    except Exception as e:
            print('==================%s'%e)
            transaction.savepoint_rollback(tran_id)
        # 返回json供前台提示成功
    return JsonResponse({'status': 1})