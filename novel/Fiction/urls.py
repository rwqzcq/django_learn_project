from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 某一类型之下的小说列表
    path('type/<int:type_id>', views.type_novels_list, name = 'type_novels_list'),
    # 某一小说的详情
    path('novelDetail/<int:novel_id>', views.novel_detail, name = 'novel_detail'),
    # 获取某一章节的内容
    path('chapterDetail/<int:chapter_id>', views.chapter_detail, name = 'chapter_detail'),
    # 获取公告列表
    path('notice', views.notice_list, name = "notice_list"),
    # 获取公告详情
    path('noticeDetail/<int:notice_id>', views.notice_detail, name = "notice_detail"),
    # 小说检索
    path('search', views.do_search, name = "do_search")
] 