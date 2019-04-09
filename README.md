## 命令
1. 创建django项目
```python
django-admin startproject 项目名
```
2. 创建超级管理员
```python
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations
# 添加项目到settings.py中的INSTALLED_APPS中去
python manage.py migrate
```

## 学习笔记
1. 设置django的后台显示为中文
> settings.py中的 LANGUAGE_CODE = 'zh-Hans'

## 工作日志
1. 添加type模型
2. 添加novel模型
3. 启动本地数据库并添加超级管理员
> 账号: admin
> 密码: admin@163.com
4. 将添加的模型注册到后台管理中去
5. 设置django的后台显示为中文
6. 上传图片配置
7. 添加章节模型
    - 富文本编辑器
    > pip install django-ckeditor
    - 设置软删除
8. 添加公告模型

9. 设置网站后台管理的名称

10. 设置列表标题显示

11. 设置系统首页的各种管理

12. 设置前台有关的操作的函数

13. 设置前台模板

14. 定义首页
> from * import * 直接用

15. 登录API
> user.is_authenticated 判断是否登录 需要在views中注入user

16. 模板继承

17. 静态资源文件加载

18. 通知公告

19. 分类



## 技术攻关
1. 集成富文本编辑器
- https://www.dusaiphoto.com/article/detail/60/
2. 上传图片
- https://blog.csdn.net/wu0che28/article/details/81542499
3. 增加编辑操作
> admin.py list_display_links属性设置
4. 数据表软删除
- https://blog.csdn.net/qq_37049781/article/details/79347278
- https://blog.csdn.net/q1242027878/article/details/74906780
5. django后台自定义设置
- https://blog.csdn.net/longdreams/article/details/78475582

6. 在models.py中设置默认添加人为当前的添加人，不需要再进行选择

7. 设置admin后台表名称和字段显示中文
- https://www.cnblogs.com/yoyoketang/p/10345479.html

8. 富文本不转义
- https://blog.csdn.net/nunchakushuang/article/details/52029521

9. 模板url传参
- https://code.ziqiangxuetang.com/django/django-template2.html

10. 上一章下一章设置
- https://www.cnblogs.com/chenchao1990/p/5311531.html?utm_source=tuicool&utm_medium=referral
- https://www.cnblogs.com/linxiyue/p/3906179.html?utm_source=tuicool&utm_medium=referral

11. 系统登录
- https://docs.djangoproject.com/zh-hans/2.2/topics/auth/default/

12. 静态资源文件
- https://www.dusaiphoto.com/article/detail/18/

13. 循环序号
- https://blog.csdn.net/hpu_yly_bj/article/details/78937884

14. 用户登录

15. 聚合查询
- https://www.cnblogs.com/guanfuchang/p/6491162.html





## 参考链接
- http://www.runoob.com/django/django-first-app.html
- https://blog.csdn.net/longdreams/article/details/78475582 
- https://www.jianshu.com/p/da94b90caad8
- https://www.cnblogs.com/yoyoketang/p/10345479.html

## 参考项目
- https://www.dusaiphoto.com/article/detail/31/

## 未完
- 后台小说菜单增加章节管理