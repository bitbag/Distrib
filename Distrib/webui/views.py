#coding=utf8
from django.shortcuts import render,redirect

# Create your views here.
from distrib_api.models import *
from vanilla import ListView, CreateView, UpdateView, DeleteView
import forms
from django.core.urlresolvers import reverse_lazy

def index(req):
    if req.user.is_authenticated():
        response = render(req,'index.html',{"username":req.user.username})
    else:
        response =redirect('login')
    return response

class Mission_ViewSet(ListView):
    Mission.objects.all().count()
    model = Mission
    template_name = 'mission.html'
    paginate_by = 10

class CreateMissionView(CreateView):
    template_name = u'mission_form.html'
    model = Mission
    form_class = forms.MissionForm
    success_url = reverse_lazy('mission-create')

    def get_context_data(self, **kwargs):
        context = super(CreateMissionView, self).get_context_data(**kwargs)

        context['title'] = u'添加应用程序'

        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'

        # login partial and commons
        context['hello'] = u'欢迎回来, '
        context['login'] = u'登录'
        context['logout'] = u'注销'

        return context
