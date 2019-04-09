from django.contrib import admin
from .models import Type, Novel, Chapter, Notice, Collection

# Register your models here.
# 设置网站后台管理的名称
admin.site.site_title="小说后台管理系统"
admin.site.site_header="小说后台管理系统"
admin.site.index_title="菜单"

# type显示
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name') # 设置显示的字段
    list_display_links = ('id', 'type_name') # 设置编辑字段
    

# 小说显示
@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'novel_type', 'author', 'intro', 'adder', 'create_time', 'update_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', ) # 设置检索字段


# 章节显示
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'intro', 'adder', 'create_time', 'update_time', 'novel', 'status')
    list_display_links = ('id', 'name')

# 公告显示
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'adder', 'create_time')
    list_display_links = ('id', 'title')

# 收藏显示
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'novel', 'create_time')
