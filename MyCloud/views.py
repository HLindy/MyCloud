from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .api import require_role
from django.contrib.auth import authenticate,login,logout
from user.views import adduser,deleteuser
from organization.models import organization
from user.models import User
@require_role(role='user')
def index(request):
    return render_to_response('index.html')


def Login(request):
    error=''
    print(request.method)
    print(request.session.get('pre_url'))
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method=='GET':
        return render_to_response('login.html')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            try:
                user=authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(user)
                        return HttpResponseRedirect(reverse(request.session.get('pre_url','/')))
                    else:
                        error="用户未激活"
            except Exception:
                    error="用户帐号或密码错误"
        else:
            error="用户账户或密码不能为空"
        return render_to_response('login.html',{'error':error})

@require_role(role='user')
def Logout(request):
    logout(request)
    return render_to_response('login.html')

def signup(request):
    error=''
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        name=request.POST.get('name','')
        phonenumber=request.POST.get('phonenumber','')
        email=request.POST.get('email','')
        organizationname=request.POST.get('organizationname','')
        role='CU'
        try:
            if not username or not password:
                error='带*不能为空'
            if organizationname!='None':
                if not organization.objects.filter(organizationname=organizationname):
                    error='组织不存在'
            if User.objects.filter(username=username):
                error='用户已存在'
        except Exception:
            pass
        else:
            try:
                adduser(username=username,password=password,name=name,
                         phonenumber=phonenumber,email=email,
                        organizationname=organizationname,role=role)
            except Exception as e:
                error='添加用户{}失败'.format(username)
                try:
                    deleteuser(username)
                except Exception:
                    pass
            else:
                return  render_to_response('login.html')
        return  render_to_response('signup.html',locals())
    if request.method=='GET':
        return render_to_response('signup.html')