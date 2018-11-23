from django.db import models

# Create your models here.

class Families(models.Model):
    '''
    family_name：姓氏
    number：该性人数
    '''
    id = models.IntegerField(primary_key=True,verbose_name='id号')
    family_name = models.CharField(max_length=32,unique=True,verbose_name='姓氏')
    number = models.CharField(max_length=32,verbose_name='数量')

    class Meta:
        db_table = 'families'


class NameMessage(models.Model):
    '''
    name:姓名
    family_name:姓氏
    number:该姓名人生
    girl_rate:女孩使用比例
    body_rate:男孩使用比例
    name_refer:姓名详解
    five:五行
    three：三才
    '''
    id = models.IntegerField(primary_key=True,verbose_name='id号')
    name = models.CharField(max_length=32,unique=True,verbose_name='姓名')
    family_name = models.CharField(max_length=16,verbose_name='姓氏')
    number = models.CharField(max_length=16,verbose_name='姓氏')
    girl_rate = models.CharField(max_length=16,verbose_name='女孩比例')
    body_rate = models.CharField(max_length=16,verbose_name='男孩比例')
    name_refer = models.CharField(max_length=1024,verbose_name='名字详解')
    five = models.CharField(max_length=32,verbose_name='五行')
    three = models.CharField(max_length=32,verbose_name='三才')

    class Meta:
        db_table = 'name_message'
