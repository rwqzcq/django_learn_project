from django.db import models
from django.contrib.auth.admin import User # 引入django的自带的User模型
from django.utils import timezone # 引入时间模型
from ckeditor.fields import RichTextField # 引入富文本编辑器

# 小说类型模型
class Type(models.Model):
    type_name = models.CharField(max_length = 32, verbose_name = '类型名称') # 定义小说类型的标题 最大长度为32

    # 在后台中只显示type_name 不显示object
    def __str__(self): 
        return self.type_name
    
    # 设置标题
    class Meta:
        verbose_name_plural = '类型管理'

# 小说模型
class Novel(models.Model):
    name = models.CharField(max_length = 32, verbose_name = '小说名') # 小说名
    novel_type = models.ForeignKey(Type, on_delete = models.DO_NOTHING, verbose_name = '小说类型') # 定义小说类型
    author = models.CharField(max_length = 32, verbose_name = '作者') # 小说作者
    intro = models.TextField() # 小说简介 
    img = models.ImageField(upload_to = 'novels', verbose_name = '封面图片', null = True) # 封面
    adder = models.ForeignKey(User, on_delete = models.DO_NOTHING, verbose_name = '添加人') # 添加人
    create_time = models.DateField(auto_now_add = True, verbose_name = '创建时间') # 创建时间
    update_time = models.DateField(auto_now = True, verbose_name = '更新时间') # 更新时间

    # 将类实例化成字符串
    def __str__(self):
        return self.name
        # return "<Novel: %s>" % self.name

    # 设置标题
    class Meta:
        verbose_name_plural = '小说管理'

# 章节模型
class Chapter(models.Model):
    name = models.CharField(max_length = 32, verbose_name = '章节名称') # 章节名称
    intro = models.TextField(verbose_name = '章节概要') # 章节概要
    content = RichTextField(verbose_name = '章节内容') # 章节内容    
    create_time = models.DateField(auto_now_add = True, verbose_name = '创建时间') # 创建时间
    update_time = models.DateField(auto_now = True, verbose_name = '更新时间') # 更新时间
    #delete_time = models.DateField(null = True,default = None) # 软删除
    adder = models.ForeignKey(User, on_delete = models.DO_NOTHING, verbose_name = '添加人') # 添加人
    novel = models.ForeignKey(Novel, on_delete = models.DO_NOTHING, verbose_name = '小说名') # 关联小说
    status = models.BooleanField(default = True, verbose_name = '状态') # 状态

    # 设置软删除
    def delete(self, using=0, keep_parents=False):
        self.status = 0
        self.save()

    def __str__(self):
        return self.name
    # 设置标题
    class Meta:
        verbose_name_plural = '章节管理'

# 公告模型
class Notice(models.Model):
    title = models.CharField(max_length = 32, verbose_name = '标题') # 公告标题
    content = RichTextField(verbose_name = '内容') # 公告内容    
    create_time = models.DateField(auto_now_add = True, verbose_name = '创建时间') # 创建时间
    adder = models.ForeignKey(User, on_delete = models.DO_NOTHING, verbose_name = '添加人') # 添加人
    
    # 设置标题
    class Meta:
        verbose_name_plural = '公告管理'

# 收藏模型
class Collection(models.Model):
    novel = models.ForeignKey(Novel, on_delete = models.DO_NOTHING, verbose_name = '小说名') # 关联小说
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, verbose_name = '收藏人') # 添加人
    create_time = models.DateField(auto_now_add = True, verbose_name = '创建时间') # 收藏时间
    
    class Meta:
        verbose_name_plural = '收藏管理'

    
    