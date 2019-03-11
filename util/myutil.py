from django.shortcuts import redirect,reverse
def authuser(fn):
    def newfn(request,*args,**kwargs):
        username = request.session.get('username',None)
        if username:
            return fn(request,*args,**kwargs)
        else:
            return redirect(reverse("pingtai:index"))
    return newfn
