from django.conf.urls import url

from hundred_family import views

urlpatterns = [
    # 姓氏页面的地址
    url(r'surnames/', views.surnames, name='surnames'),
    # 名字页面的地址
    url(r'names/(.+)/', views.names, name='names'),
    # 名字详解的地址
    url(r'info/(.+)/', views.info, name='info'),
    # 名字详解页面得到数据
    url(r'name_messages/(.+)/', views.name_messages, name='name_messages'),
]