from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
import os.path
from userauth.models import User as Us
from pingtai.models import Category,keyword
from django.conf import settings   #在blog里的都是配置项conf,因此需要这样引
# from django.views.decorators

# Create your views here.
from util.myutil import authuser
from .forms import ArticleForm,User

@authuser
def index(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/index.html', {'name': name})

@authuser
def lianjie(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/lianjie.html', { 'name': name})

@authuser
def selfadmin(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/index.html', { 'name': name})
@authuser
def selfinfo(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/selfinfo.html', { 'name': name})

@authuser
def liuyan(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/liuyan.html', { 'name': name})

@authuser
def guanli(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/guanli.html', { 'name': name})

@authuser
def passed(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/passed.html', {'name': name})

# @authuser
# def upload(request):
#   if request.method == 'POST':
#     img=request.FILES['img']
#     name=img.name
#     with open('uploads/%s'%name,'wb+') as destination:
#       for chunk in img.chunks():
#         destination.write(chunk)
#     return HttpResponse("ok")

@authuser
def upload(request):
  if request.method == 'GET':
    name = request.session.get('name', None)
    return render(request, 'self/upload.html', {'name': name})

@authuser
def img(request):
    name = request.session.get('username', None)
    names=name
    if request.is_ajax():
      img = request.FILES.get('upload',None)
      name=os.path.join("uploads","userimg",img.name)
      if img:
        with open(name,"wb+") as f:   #拼接成一个路径
          for chunk in img.chunks():
            f.write(chunk)
            Us.objects.filter(username=names).update(img=os.path.join("userimg",img.name))
      return JsonResponse({"status":"ok","src":os.path.join(settings.MEDIA_URL,'userimg',img.name)})


def article(request):
  username = request.session.get('username', None)
  if request.method == 'GET':
    uobj=Us.objects.filter(username=username).first()
    articles=uobj.article_set.all()
    c=Category.objects.all()
    k=keyword.objects.all()
    return render(request, 'self/article.html',{'articles':articles,'c':c,'k':k})

@authuser
def addArticle(request):
  username = request.session.get('username', None)
  cate = Category.objects.all()
  if request.method == 'GET':
    form = ArticleForm()
    return render(request, 'self/addArticle.html',{'form':form,'cate':cate})
  else:
    form=ArticleForm(request.POST)
    if form.is_valid():
      obj=form.save(commit=False)
      obj.a_id = User.objects.filter(username=username).first().id
      obj.save()
      return redirect(reverse('self:addArticle'))
    return render(request, 'self/addArticle.html', {'form': form,'cate':cate})


def loginout(request):
  del request.session['username']
  return redirect(reverse('pingtai:index'))
