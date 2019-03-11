from django.db import models
from userauth.models import User
from pingtai.models import PTArticle,Category,keyword
from ckeditor.fields import RichTextField

class Article(models.Model):
  c = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='分类')
  k = models.ForeignKey(to=keyword, on_delete=models.CASCADE, verbose_name='关键字')
  a = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='作者')
  title = models.CharField(max_length=50, verbose_name='文章标题')
  con = RichTextField(max_length=30000, verbose_name='文章内容')
  c_time = models.DateTimeField(auto_now_add=True)
  u_time = models.DateTimeField(auto_now=True)
  status = models.BooleanField(default=False, verbose_name='发布状态')
  look = models.IntegerField(default=0)




