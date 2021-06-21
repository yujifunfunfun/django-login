from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm

class Top(generic.TemplateView):
    template_name = 'register/top.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'register/top.html'

class Index(LoginRequiredMixin, generic.ListView):
    def get(self,request):
      return render(request, 'register/index.html')

class Mypage(LoginRequiredMixin, generic.ListView):
    def get(self,request):
      return render(request, 'register/mypage.html')