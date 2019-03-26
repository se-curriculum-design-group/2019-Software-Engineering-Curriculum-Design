from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class Sending_Emails(forms.Form):
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