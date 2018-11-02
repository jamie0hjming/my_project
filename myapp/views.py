from django.shortcuts import render

# Create your views here.
from myapp.models import Wheel, Nav, Mustbuy, Shop, Mainshow


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    must_buys = Mustbuy.objects.all()
    shop = Shop.objects.all()
    shophead = shop[0]
    shoptabs = shop[1:3]
    shopclasss = shop[3:7]
    shopcommends = shop[7:]

    mainshows =Mainshow.objects.all()


    data = {
        'wheels': wheels,
        'navs': navs,
        'must_buys': must_buys,
        'shophead':shophead,
        'shoptabs': shoptabs,
        'shopclasss': shopclasss,
        'shopcommends': shopcommends,
        'mainshows':mainshows
        }
    return render(request,'home/home.html',context = data)


def cart(request):
    return render(request,'cart/cart.html')


def market(request):
    return render(request,'market/market.html')


def mine(request):
    return render(request,'mine/mine.html')