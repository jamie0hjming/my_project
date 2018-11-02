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
