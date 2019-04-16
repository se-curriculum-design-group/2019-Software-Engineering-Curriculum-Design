from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
import re


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class SendEmails(forms.Form):
    dep = (
        ('0', '全体成员用户'),
        ('1', '信息科学与技术学院'),
        ('2', '化学工程学院'),
        ('3', '材料科学与工程学院'),
        ('4', '机电工程学院'),
        ('5', '经济管理学院'),
        ('6', '理学院'),
        ('7', '文法学院'),
        ('8', '生命科学与技术学院'),
        ('9', '继续教育学院'),
        ('10', '马克思主义学院'),
        ('11', '国际教育学院'),
        ('12', '侯德榜工程师学院'),
        ('13', '能源学院'),
        ('14', '巴黎居里工程师学院'),
    )
    receiver = forms.ChoiceField(label='收件人', choices=dep)
    title = forms.CharField(label="主题", max_length=128,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    text = forms.CharField(
        label="正文",
        widget=forms.Textarea(attrs={
            'style': 'height: 100%;width:100%'}))
    attach = forms.FileField(label="附件选择", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class SearchAnnouncement(forms.Form):
    text = forms.CharField(label="公告查找", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           initial="")


class AddAnnouncement(forms.Form):
    dep = (
        ('全体成员', '全体成员'),
        ('信息科学与技术学院', '信息科学与技术学院'),
        ('化学工程学院', '化学工程学院'),
        ('材料科学与工程学院', '材料科学与工程学院'),
        ('机电工程学院', '机电工程学院'),
        ('经济管理学院', '经济管理学院'),
        ('理学院', '理学院'),
        ('文法学院', '文法学院'),
        ('生命科学与技术学院', '生命科学与技术学院'),
        ('继续教育学院', '继续教育学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('国际教育学院', '国际教育学院'),
        ('侯德榜工程师学院', '侯德榜工程师学院'),
        ('能源学院', '能源学院'),
        ('巴黎居里工程师学院', '巴黎居里工程师学院'),
        ('个人', '个人'),
    )
    years = (
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )
    receiver = forms.ChoiceField(label='通知对象组织', choices=dep)
    year = forms.ChoiceField(label="通知对象入学年份", choices=years)
    individual = forms.CharField(label="通知个人学号(选填)", max_length=32, required=False)
    title = forms.CharField(label="通知主题", max_length=128,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    text = forms.CharField(
        label="通知正文",
        widget=forms.Textarea(attrs={
            'style': 'height: 100%;width:100%'}))


class Searchper(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))


class DetailForm1(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    dep = (
        ('信息科学与技术学院', '信息科学与技术学院'),
        ('化学工程学院', '化学工程学院'),
        ('材料科学与工程学院', '材料科学与工程学院'),
        ('机电工程学院', '机电工程学院'),
        ('经济管理学院', '经济管理学院'),
        ('理学院', '理学院'),
        ('文法学院', '文法学院'),
        ('生命科学与技术学院', '生命科学与技术学院'),
        ('继续教育学院', '继续教育学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('国际教育学院', '国际教育学院'),
        ('侯德榜工程师学院', '侯德榜工程师学院'),
        ('能源学院', '能源学院'),
        ('巴黎居里工程师学院', '巴黎居里工程师学院'),
    )

    gra = (
        ('1', 'top'),
        ('2', 'middle'),
        ('3', 'ordinary'),
    )
    password1 = forms.CharField(label="新密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认新密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    building = forms.ChoiceField(label='学院', choices=dep)
    grant = forms.ChoiceField(label='授权', choices=gra)
    captcha = CaptchaField(label='验证码')


class DetailForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    dep = (
        ('信息科学与技术学院', '信息科学与技术学院'),
        ('化学工程学院', '化学工程学院'),
        ('材料科学与工程学院', '材料科学与工程学院'),
        ('机电工程学院', '机电工程学院'),
        ('经济管理学院', '经济管理学院'),
        ('理学院', '理学院'),
        ('文法学院', '文法学院'),
        ('生命科学与技术学院', '生命科学与技术学院'),
        ('继续教育学院', '继续教育学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('国际教育学院', '国际教育学院'),
        ('侯德榜工程师学院', '侯德榜工程师学院'),
        ('能源学院', '能源学院'),
        ('巴黎居里工程师学院', '巴黎居里工程师学院'),
    )

    password0 = forms.CharField(label="原密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="新密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认新密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )

    start = (
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    )

    time = (
        ('4年制', '4年制'),
        ('5年制', '5年制'),
        ('6年制', '6年制'),
    )

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    name = forms.CharField(label='name', max_length=50)
    sex = forms.ChoiceField(label='性别', choices=gender)
    age = forms.CharField(label='age', max_length=50)
    start_year = forms.ChoiceField(label="入学年份", choices=start)
    length = forms.ChoiceField(label="学制", choices=time)
    major = forms.CharField(label='主修', max_length=50)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 character long.")
        elif len(username) > 50:
            raise forms.ValidationError("Your username is too long")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your email already exists")
        else:
            raise forms.ValidationError("Please enter a Valid email")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password missmatch. Please enter again")
        return password2


class TeacherForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )

    dep = (
        ('1', '信息科学与技术学院'),
        ('2', '化学工程学院'),
        ('3', '材料科学与工程学院'),
        ('4', '机电工程学院'),
        ('5', '经济管理学院'),
        ('6', '理学院'),
        ('7', '文法学院'),
        ('8', '生命科学与技术学院'),
        ('9', '继续教育学院'),
        ('10', '马克思主义学院'),
        ('11', '国际教育学院'),
        ('12', '侯德榜工程师学院'),
        ('13', '能源学院'),
        ('14', '巴黎居里工程师学院'),
    )
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    name = forms.CharField(label='name', max_length=50)
    sex = forms.ChoiceField(label='性别', choices=gender)
    title = forms.CharField(label='title', max_length=128)
    department = forms.ChoiceField(label='学院', choices=dep)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 character long.")
        elif len(username) > 50:
            raise forms.ValidationError("Your username is too long")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your email already exists")
        else:
            raise forms.ValidationError("Please enter a Valid email")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password missmatch. Please enter again")
        return password2
