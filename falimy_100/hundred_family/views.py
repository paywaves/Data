import json

from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from hundred_family.models import Families, NameMessage

#姓氏页面获取数据
def surnames(request):
    if request.method == 'GET':
        # 从数据库获取所有姓氏和姓名个数
        surnames = Families.objects.all()
        # 分组 每组7条数据
        surname_list = []
        name_list = []
        for surname in surnames:
            name_list.append(surname)
            if len(name_list) == 7:
                surname_list.append(name_list)
                name_list = []
        return render(request,'index.html',{'surnames':surname_list})


#获取指定姓氏的所有名字
def names(request,surname):
    if request.method == 'GET':
        # 从数据库获取指定姓氏的名字及详细信息
        messages = NameMessage.objects.filter(family_name=surname)
        # 过滤数据，只留姓名
        names = []
        for message in messages:
            names.append(message.name)
        # 分组 每组15条数据
        names_list = []
        name_list = []
        for name in names:
            name_list.append(name)
            if len(name_list) == 15:
                names_list.append(name_list)
                name_list = []
        # 获得页面数
        page_number = request.GET.get('page', 1)
        # 分页 每页取20个
        paginator = Paginator(names_list, 20)
        pages = paginator.page(page_number)
        return render(request,'names.html',{'pages':pages,'surname':surname})


def info(request,name):
    if request.method == 'GET':
        return render(request,'info.html')


def name_messages(request,name):
    if request.method  == 'GET':
        message = NameMessage.objects.filter(name=name).values('name','family_name','number','girl_rate','body_rate','name_refer','five','three')
        return JsonResponse({'code':200,'message':message[0]})