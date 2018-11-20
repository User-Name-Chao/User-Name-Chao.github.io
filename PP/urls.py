
from django.conf.urls import url

from PP import views
urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^regist/', views.regist, name="regist"),
    url(r'^loginout/', views.loginout, name="loginout"),
]






















