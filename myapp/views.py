from django.shortcuts import render

# Create your views here.
from myapp.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


# 主页

def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    must_buys = Mustbuy.objects.all()
    shop = Shop.objects.all()
    shophead = shop[0]
    shoptabs = shop[1:3]
    shopclasss = shop[3:7]
    shopcommends = shop[7:]

    mainshows = Mainshow.objects.all()

    data = {
        'wheels': wheels,
        'navs': navs,
        'must_buys': must_buys,
        'shophead': shophead,
        'shoptabs': shoptabs,
        'shopclasss': shopclasss,
        'shopcommends': shopcommends,
        'mainshows': mainshows
    }
    return render(request, 'home/home.html', context=data)


# 购物车
def cart(request):
    return render(request, 'cart/cart.html')


# 闪购超市
# 三个参数
# category_id 分类ID
# child_id 子类ID
# sort_id 排序ID

def market(request, category_id, child_id, sort_id):
    print(category_id)
    # 点击侧栏客户端传送的侧栏下标，默认为0
    type_index = request.COOKIES.get('type_index', 0)
    # 得到所有侧栏主类
    food_types = Foodtypes.objects.all()

    # print(child_type_id_list)

    food_type = food_types[int(type_index)]  # 得到对应主类
    category_id = food_type.type_id  # 对应主类Id
    # 判断主类和子类，子类中开始默认全部

    child_type_id = food_type.child_type_names
    child_type_id_list = child_type_id.split('#')
    child_type_id_name_list = []
    for name_id in child_type_id_list:  # 得到子类含有子类name和id 并存入列表
        dic = {
            'type_child_name': name_id.split(':')[0],
            'type_child_id': int(name_id.split(':')[1]),
        }
        child_type_id_name_list.append(dic)

    # goods = Goods.objects.filter(category_id=int(category_id))  # 根据主类ID 得到该主类ID下所有的商品
    if int(child_id):
        goods = Goods.objects.filter(category_id=int(category_id), child_id=int(child_id))
    else:
        goods = Goods.objects.filter(category_id=int(category_id))  # 根据主类ID 得到该主类ID下所有的商品

        # print(child_type_id_name_dict)

    if sort_id == '1':  # 销量排序
        goods = goods.order_by('-product_num')
    elif sort_id == '2':  # 价格最低
        goods = goods.order_by('price')
    elif sort_id == '3':  # 价格最高
        goods = goods.order_by('-price')

    data = {

        'food_types': food_types,
        'goods': goods,
        'child_type_id_name_list': child_type_id_name_list,
        'category_id': category_id,
        'child_id': child_id,
        'sort_id': sort_id,
    }
    return render(request, 'market/market.html', context=data)


# 我的

def mine(request):
    return render(request, 'mine/mine.html')
