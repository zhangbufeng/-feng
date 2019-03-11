from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm
def login(request):
    if request.method=="GET":
        form=LoginForm()
        return render(request,'userauth/login.html',{'form':form})
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            request.session['username']=username
            return redirect(reverse("pingtai:index"),{'form':form})
        else:
            return render(request,'userauth/login.html',{'form':form})
def regist(request):
    if request.method=="GET":
        form=RegisterForm()
        return render(request,'userauth/register.html',{"form":form})
    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("userauth:login"))
        else:
            return redirect(reverse("userauth/register.html"),{"form":form})
def loginout(request):
    del request.session['username']
    return redirect(reverse('pingtai:index'))