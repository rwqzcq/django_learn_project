from django import forms

# 公共form文件

# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label = '用户名')
    password = forms.CharField(label = '密码', widget = forms.PasswordInput)
