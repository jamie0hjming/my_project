from django.db import models

# Create your models here.
class Base(models.Model):

    img = models.CharField(max_length=256) # 图片路径
    name = models.CharField(max_length=100)
    track_id = models.CharField(max_length=20)

    # 通过一个内嵌类 "class Meta" 给你的 model 定义元数据,db_table是用于指定自定义数据库表名的
    class Meta:

        # 如果你想把某些公共信息添加到很多 model 中，抽象基类就显得非常有用。你编写完基类之后，
        # 在 Meta 内嵌类中设置 abstract=True ，该类就不能创建任何数据表。然而如果将它做为其他 model
        #  的基类，那么该类的字段就会被添加到子类中。抽象基类和子类如果含有同名字段，就会导致错误(Django 将抛出异常)。
        abstract = True

# 继承时，Django 会对基类的 Meta 内嵌类做一个调整：在安装 Meta 属性之前，Django 会设置 abstract=False。
# 这意味着抽象基类的子类不会自动变成抽象类。当然，你可以让一个抽象类继承另一个抽象基类，不过每次都要显式地设置
# abstract=True 。对于抽象基类而言，有些属性放在 Meta 内嵌类里面是没有意义的。
# 例如，包含 db_table 将意味着所有的子类(是指那些没有指定自己的 Meta 内嵌类的子类)都使用同一张数据表，
# 一般来说，这并不是我们想要的。

class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

class Mainshow(models.Model):
    track_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=256)
    category_id = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)

    img1 = models.CharField(max_length=256)
    child_id1 = models.CharField(max_length=20)
    product_id1 = models.CharField(max_length=20)
    long_name1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    market_price1 = models.FloatField()

    img2 = models.CharField(max_length=256)
    child_id2 = models.CharField(max_length=20)
    product_id2 = models.CharField(max_length=20)
    long_name2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    market_price2 = models.FloatField()

    img3 = models.CharField(max_length=256)
    child_id3 = models.CharField(max_length=20)
    product_id3 = models.CharField(max_length=20)
    long_name3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    market_price3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

class Foodtypes(models.Model):
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=100)
    child_type_names = models.CharField(max_length=256)
    type_sort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    product_id = models.IntegerField()  # 商品ID
    product_img = models.CharField(max_length=100)  # 商品图片
    product_name = models.CharField(max_length=100)  # 商品名称
    product_long_name = models.CharField(max_length=100)  # 商品弄名称
    is_xf = models.BooleanField(default=False)  # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)  # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)  # 价格
    market_price = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    category_id = models.IntegerField()  # 分类ID
    child_id = models.IntegerField()  # 子类ID
    child_id_name = models.CharField(max_length=100)  # 分类名称
    dealer_id = models.IntegerField()  # 详情ID
    store_nums = models.IntegerField()  # 库存
    product_num = models.IntegerField()  # 销量

    class Meta:
        db_table = 'axf_goods'




class User(models.Model):
    account = models.CharField(max_length=80, unique=True)  # 账号 唯一约束
    password = models.CharField(max_length=256)  # 密码
    name = models.CharField(max_length=100)  # 名字
    phone = models.CharField(max_length=20, unique=True)  # 手机号 唯一约束
    addr = models.CharField(max_length=256)  # 地址
    img = models.CharField(max_length=100)  # 头像
    rank = models.IntegerField(default=1)  # 等级
    token = models.CharField(max_length=256)  # token

    class Meta:
        db_table = 'axf_user'


class Cart(models.Model):
    user = models.ForeignKey(User)  # 用户外键关联
    goods = models.ForeignKey(Goods)  # 商品外建关联
    num = models.IntegerField()  # 选购的商品数量
    is_select = models.BooleanField(default=True)  # 是否被选中

    class Meta:
        db_table = 'axf_cart'




class Order(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    # 状态
    # -1 过期
    # 1 未付款
    # 2 已付款，未发货
    # 3 已发货，快递
    # 4 已签收，未评价
    # 5 已评价
    # 6 退款....
    status = models.IntegerField(default=1)
    # 订单号
    identifier = models.CharField(max_length=256)


# 订单商品
# 一个订单 对应 多个商品
# 在从表中声明关系
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(Goods)
    # 个数
    number = models.IntegerField(default=1)

    # 大小
    # 颜色