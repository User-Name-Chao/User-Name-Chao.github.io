import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from PP.models import User

def index(request):
    datas = {
        'title': '主页',

    }
    userid = request.session.get('user_id')

    users = User.objects.filter(pk=userid)

    if users.exists():
        user = users.first()

        datas['username'] = user.username
        datas['icon'] = '/static/uploadfiles/' + user.icon.url
        datas['is_login'] = True
        return render(request, 'index.html', context=datas)
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username)

        if users.exists():
            user = users.first()

            if user.password == make_pwd(password):
                request.session['user_id'] = user.id

                return redirect(reverse('PP:index'))

        # return render(request,'regist.html')
    return HttpResponse("无效请求")


def regist(request):
    if request.method == "GET":
        return render(request, 'regist.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        print(username)
        print(password)
        print(email)
        print(icon)

        user = User()

        user.username = username
        user.password = make_pwd(password)
        user.email = email
        user.icon = icon

        user.save()
        request.session["user_id"] = user.id
    return render(request, 'index.html')

def make_pwd(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def loginout(request):

    request.session.flush()
    # return render(request, 'index.html')
    return redirect(reverse('PP:index'))