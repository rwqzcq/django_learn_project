from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from .models import Novel, Chapter, Type, Notice, Collection
from django.db.models import Min, Sum
from django.db.models import Max
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # 登录限制

# 首页
def index(request):
    context = {}
    # 找到最多小说的前三个分词
    novel_list = Novel.objects.values('novel_type').annotate()[0:3]
    id_ins = []
    for type in novel_list:
        print(type['novel_type'])
        id_ins.append(type['novel_type'])
    context['most_types'] = Type.objects.filter(id__in = id_ins)
    context['all_types'] = Type.objects.all()
    # 最新公告 5条
    context['new_notices'] = Notice.objects.order_by('-create_time')[0:5]
    # 最新发布 4条
    context['new_novels'] = Novel.objects.order_by('-create_time')[0:4]
    # 找到登陆者
    context['user'] = request.user
    return render(request,'index.html', context)

# 类别
def type_list(request):
    #context = {}
    #context['types'] = Type.objects.all()
    #return render_to_response('blog_list.html', context)
    pass

# 某一类别下的小说列表
def type_novels_list(request, type_id):
    context = {}
    context['type'] = get_object_or_404(Type, pk = type_id)
    context['novelLists'] = Novel.objects.filter(novel_type = type_id)
    return render(request,'novel_list.html', context)

# 获取小说整体情况
def novel_detail(request, novel_id):
    context = {}
    # 获取小说的概况
    context['novel'] = get_object_or_404(Novel, pk = novel_id)
    # 获取小说的章节
    context['chapters'] = Chapter.objects.filter(novel = novel_id)
    # 查看当前的小说作者是否已经收藏
    is_collect = False
    if request.user.is_authenticated == True:
        is_collect = Collection.objects.filter(novel = context['novel'], user = request.user)
    if is_collect:
        context['is_collect'] = True
    else:
        context['is_collect'] = False
    return render(request, 'novel_detail.html', context)

# 获取小说章节
# def chapter_list(request, novel_id):
#     pass

# 获取小说章节具体内容
def chapter_detail(request, chapter_id):
    context = {}
    chapter = get_object_or_404(Chapter, pk = chapter_id)
    context['chapter'] = get_object_or_404(Chapter, pk = chapter_id)
    # 找到下一章
    novel_id = chapter.novel
    next_id = Chapter.objects.filter(novel = novel_id, id__gt = chapter_id).aggregate(Min('id'))
    context['next_chapter'] = next_id
    # 找到上一章
    former_id = Chapter.objects.filter(novel = novel_id, id__lt = chapter_id).aggregate(Max('id'))
    context['former_chapter'] = former_id
    # 返回小说详情
    return render(request,'chapter_detail.html', context)

# 用户登录页
def login_page(request):
    return render(request, 'login.html')

# 用户登录
def do_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)
    user = authenticate(username = username, password = password) # 认证
    print(user)
    if user is not None:
        # 设置session
        login(request, user)
        refer = request.META.get('HTTP_REFERER', '/')
        print(refer)
        return redirect(refer) # 跳转到首页
    else:
        # 返回错误信息
        return render(request, 'index.html')
# 用户退出登录
def user_logout(request):
    logout(request)
    js = '<script>alert("退出登录成功!");location.href = "/"</script>'
    return HttpResponse(js)
# 用户注册
def register_page(request):
    return render(request, 'register.html')



# 用户注册
def do_register(request):
    user_register_form = UserRegisterForm(data=request.POST)
    if user_register_form.is_valid():
        new_user = user_register_form.save(commit=False)
        new_user.set_password(user_register_form.cleaned_data['password'])
        new_user.save()
        # 返回登录页面
        return HttpResponse('<script>alert("注册成功!请先登录");location.href = "/login"</script>')
    else:
        return HttpResponse('<script>alert("表单输入的信息有误!请重新填写!");location.href = "/register"</script>')

# 公告列表
def notice_list(request):
    context = {}
    context['notice_list'] = Notice.objects.order_by('-create_time')
    return render(request, 'notice_list.html', context)

# 公告详情
def notice_detail(request, notice_id):
    context = {}
    # 获取小说的概况
    context['notice'] = get_object_or_404(Notice, pk = notice_id)
    print(notice_id)
    return render(request, 'notice_detail.html', context)

# 进行收藏
@login_required(login_url='/login')
def do_collect(request, novel_id) :
    # 判断是否已经收藏
    novel = get_object_or_404(Novel, pk = novel_id)
    is_collect = Collection.objects.filter(user = request.user, novel = novel)
    if is_collect:
        js = '<script>alert("已经收藏!");window.location.href="/fiction/novelDetail/' + str(novel_id) + '"</script>'
        return HttpResponse(js)
    collect = Collection(user = request.user, novel = novel)
    collect.save()
    js = '<script>alert("收藏成功");window.location.href="/fiction/novelDetail/' + str(novel_id) + '"</script>'
    return HttpResponse(js)

# 收藏列表
@login_required(login_url='/login')
def collect_list(request):
    context = {}
    context['collections'] = Collection.objects.filter(user = request.user)
    return render(request, 'my_collection.html', context)

# 检索
def do_search(request):
    name = request.POST.get('name', '')
    context = {}
    context['novelLists'] = Novel.objects.filter(name__contains = name)
    context['keyword'] = name
    context['count'] = len(context['novelLists'])
    return render(request, 'search_list.html', context)
