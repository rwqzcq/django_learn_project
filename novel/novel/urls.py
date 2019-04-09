"""novel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Fiction.views import index
from Fiction.views import login_page
from Fiction.views import do_login, user_logout, register_page, do_register, collect_list, do_collect

urlpatterns = [
    path('', index, name = "index"), # 定义首页
    path('admin/', admin.site.urls), # 定义后台管理页
    path('fiction/', include('Fiction.urls')), # 定义小说模块页
    path('login', login_page, name = "login"), # 登录页面
    path('do_login', do_login, name = "do_login"), # 执行登录
    path('logout', user_logout, name = "logout"), # 制定退出登录的操作
    path('register', register_page, name = "register"), # 注册页面
    path('do_register', do_register, name = "do_register"), # 执行注册
    path('collect', collect_list, name = "my_collect"), # 收藏列表
    path('do_collect/<int:novel_id>', do_collect, name = "do_collect"), # 进行收藏

]
