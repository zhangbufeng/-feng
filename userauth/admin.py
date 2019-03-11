from django.contrib import admin
from .models import User
from pingtai.models import UserInfo
# Register your models here.


@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
  fields = ['u','realname']
  # readonly_fields = ['u','realname']
  list_display = ['u','company','realname','position','honny','reason','sh']
  list_editable = ['sh']
  list_per_page = 2
  list_filter = ['u', 'sh']
  def wsh(self,request,queryset):
    queryset.update(sh=0)
  def shz(self,request,queryset):
    queryset.update(sh=1)
  def shtg(self,request,queryset):
    queryset.update(sh=2)
  wsh.short_description='未审核'
  shz.short_description = '审核中'
  shtg.short_description = '审核通过'
  actions = ['wsh','shz','shtg']
