from django.conf.urls import url

from myapp import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^mine/$', views.mine, name='mine'),
    url(r'^registe/$', views.registe, name='registe'),  # 注册
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),  # 账号验证
    url(r'^logout/$', views.logout, name='logout'),  # 退出
    url(r'^login/$', views.login, name='login'),  # 登录
    url(r'^addgoods/$', views.addgoods, name='addgoods'),  # 添加购物车
    url(r'^subgoods/$', views.subgoods, name='subgoods'),  # 购物车减操作
    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'),  # 修改选中状态
    url(r'changecartselect/$', views.changecartselect, name='changecartselect'),  # 全选/取消全选
    url(r'^generateorder/$',views.generateorder,name='generateorder'),  # 订单提交
    url(r'^order/(\d+)/$', views.order, name='order'),

]
