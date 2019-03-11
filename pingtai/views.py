from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import keyword,Category,PTArticle,UserInfo,Ping
from userauth.models import User
from django.http import HttpResponse
from .forms import UserInfoForm
from .fangjia1 import reg
import pandas as pd
import os
# Create your views here.
def index(request):
    if request.method=='GET':
        data=Category.getAll()
        article=PTArticle.objects.all()
        username=request.session.get("username")
        userInfo=UserInfo.objects.all()
        return render(request,"pingtai/index.html",{'data':data,'article':article,'username':username,'userinfo':userInfo})

@csrf_exempt
def getKeyword(request):
    if request.is_ajax():
        c=request.POST.get('c',None)
        res=keyword.objects.filter(c=c).values_list('id','name')
        obj={}
        for arr in res:
            obj[arr[0]]=arr[1]
        return JsonResponse(obj)

def detail(request,con_id):
    con=PTArticle.objects.filter(id=con_id).first()
    return render(request,'pingtai/xiangqing.html',{"con":con})

def kaitong(request):
    if request.method == "GET":
        username = request.session.get("username",None)
        if username:
            obj=User.objects.filter(username=username).first()
            c=obj.c
            if int(c)==0:
                form=UserInfoForm({'u':obj.id,'sh':1})
                return render(request,'pingtai/kaitong.html',{'form':form})
            else:
              return HttpResponse('用户后台')
        else:
            return redirect(reverse("userauth:login"))
    else:
        form=UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            #username = request.session.get("username", None)
            #User.objects.filter(username=username).update()
            return redirect(reverse("pingtai:index"))
        else:
            return render(request, 'pingtai/kaitong.html', {'form': form})

from sklearn.linear_model import LinearRegression
def links(request):
  if request.method == 'GET':
    return render(request, 'pingtai/links.html')
  else:
    dist = request.POST.get("dist")
    if dist == 'dist_dongcheng':
      dist = '10000'
    elif dist == 'dist_fengtai':
      dist = '01000'
    elif dist == 'dist_haidian':
      dist = '00100'
    elif dist == 'dist_shijingshan':
      dist = '00010'
    elif dist == 'dist_xicheng':
      dist = '00001'
    elif dist == 'dist_chaoyang':
      dist = '00000'
    data = []
    roomnum = request.POST.get("roomnum")
    halls = request.POST.get("halls")
    area = request.POST.get("area")
    floor = request.POST.get("floor")
    if floor == 'floor_low':
      floor = '10'
    elif floor == 'floor_middle':
      floor = '01'
    elif floor == 'floor_high':
      floor = '00'
    subway = request.POST.get("subway")
    school = request.POST.get("school")
    for i in dist:
      data.append(int(i))
    data.append(int(roomnum))
    data.append(int(halls))
    data.append(float(area))
    for i in floor:
      data.append(int(i))
    data.append(int(subway))
    data.append(int(school))
    df = pd.read_csv(os.path.join("uploads",'house_price.csv'))
    df1=pd.get_dummies(df[['dist','floor']])
    del df1["dist_chaoyang"]
    del df1["floor_high"]
    df2 = pd.concat([df1, df], axis=1)
    del df2["dist"]
    del df2["floor"]
    X = df2.iloc[:, :-1]
    # print(X.head())
    y = df2["price"]
    from sklearn.linear_model import LinearRegression  # 普通最小二乘线性回归
    reg = LinearRegression(normalize=True)  # 岭回归
    reg = reg.fit(X, y)
    result=int(reg.predict([data])[0])
    print(reg.score(X,y))
    return render(request, 'pingtai/links.html',{'dist':dist,'roomnum':roomnum,'halls':halls,'floor':floor,'area':area,'subway':subway,'school':school,'price':result})


