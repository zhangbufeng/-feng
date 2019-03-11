from django.contrib import admin
from .models import Category,keyword,PTArticle
# Register your models here.

admin.AdminSite.site_header='博客社区'
admin.AdminSite.site_title='我的博客'
admin.AdminSite.index_title='博客后台管理'

class KeywordInline(admin.StackedInline):
    model = keyword
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields=['name']
    list_display = ['name','listKeyword']
    inlines =[KeywordInline]
@admin.register(PTArticle)
class PTArticle(admin.ModelAdmin):
    exclude = []
    list_display = ['title','c','k','status','a','c_time','u_time']
    # readonly_fields = ['a']
    radio_fields = {"a":admin.HORIZONTAL}
    class Media:
        js=('pingtai/js/addPTArticle.js',)
    list_per_page = 2
    list_filter = ('a','c','k')
    date_hierarchy='u_time'
    search_fields = ['title']
    add_form_template = 'admin/addPTArticle.html'
    def add_view(self, request, form_url='', extra_context=None):
        return super().add_view(request,form_url,extra_context)
    def save_model(self, request, obj, form, change):
        obj.a=request.user
        return super().save_model(request,obj,form,change)
    def fabu(self,request,queryset):
        queryset.update(status=True)
    def chehui(self,request,queryset):
        queryset.update(status=False)
    chehui.short_description = '撤回发布'
    fabu.short_description = '发布'
    actions = [fabu,chehui]