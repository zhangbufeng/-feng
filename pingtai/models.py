from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name=models.CharField(verbose_name='分类',max_length=20)
    def listKeyword(self):
        objs=self.keyword_set.all()
        arr=[]
        for item in objs:
            arr.append("<e style='margin:0 5px'>"+item.name+"</e>")
        return format_html("".join(arr))
    listKeyword.short_description='关键字'
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="分类管理"
        verbose_name_plural = "分类管理"

    @classmethod
    def getAll(cls):
        return cls.objects.all()


class keyword(models.Model):
    name = models.CharField(verbose_name='关键字',max_length=20)
    c=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PTArticle(models.Model):
    c=models.ForeignKey(verbose_name='分类',to=Category,on_delete=models.CASCADE)
    k=models.ForeignKey(verbose_name='关键字',to=keyword,on_delete=models.CASCADE)
    a=models.ForeignKey(verbose_name='作者',to=User,on_delete=models.CASCADE)
    title=models.CharField(verbose_name='文章标题',max_length=50)
    con=RichTextField(verbose_name='文章内容',max_length=20000)
    c_time=models.DateTimeField(auto_now_add=True)
    u_time=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False,verbose_name='发布状态')
    class Meta:
        verbose_name="文章管理"
        verbose_name_plural = "文章管理"

    @classmethod
    def getAll(cls):
        return cls.objects.filter(status=True)
from userauth.models import User
class UserInfo(models.Model):
    u=models.OneToOneField(to=User,on_delete=models.CASCADE,verbose_name="用户")
    company=models.CharField(max_length=20,verbose_name="公司")
    position=models.CharField(max_length=20,verbose_name="职位")
    honny=models.CharField(max_length=20,verbose_name="爱好")
    reason=models.TextField(max_length=200,verbose_name="申请理由")
    realname = models.CharField(max_length=10, verbose_name="真实姓名")
    sh=models.IntegerField(default=1,choices=(
        (0,"未审核"),
        (1,"审核中"),
        (2,"审核通过"),
    ))
    class Meta:
        verbose_name="开通管理"
        verbose_name_plural = "开通管理"

    @classmethod
    def getAll(cls):
        return cls.objects.all()
class Ping(models.Model):
    c = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='评论用户')
    e = models.ForeignKey(to=PTArticle, on_delete=models.CASCADE, verbose_name='文章')
    nei = models.CharField(max_length=2000, verbose_name='评论内容')
    ctime = models.DateTimeField(auto_now_add=True)

    @classmethod
    def getAll(cls):
        return cls.objects.all()