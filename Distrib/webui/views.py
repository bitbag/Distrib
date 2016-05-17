#coding=utf8
from django.shortcuts import render,redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponseRedirect
from django.db.models import Q
from distrib_api.models import *
from vanilla import ListView, CreateView, UpdateView, DeleteView,FormView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
import json
import forms
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

    def get_queryset(self):
        # support search
        try:
            keyword = self.request.GET['keyword']
        except:
            keyword = ''
        if keyword == '':
            return Mission.objects.all()
        else:
            return Mission.objects.filter(Q(version__icontains=keyword))

class CreateMissionView(FormView):
    template_name = u'mission_form.html'
    model = Mission
    form_class = forms.MissionForm
    success_url = reverse_lazy('mission')

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



    def form_valid(self, form):
        version = form.cleaned_data['version']
        remark = form.cleaned_data['remark'] if True else None
        groups = form.cleaned_data['groups']
        hosts = form.cleaned_data['hosts']
        playbooks = form.cleaned_data['playbooks']
        Instance = Mission.objects.create(version=version, remark=remark,
                                          status=Status.objects.get(name='init'))
        Instance.save()
        try:
            for group in groups:
                Instance.groups.add(group)
            for host in hosts:
                Instance.hosts.add(host)
            for plabook in playbooks:
                Instance.playbooks.add(plabook)
        except Exception as e:
            form.add_error(None, e.message)
            Instance.status=Status.objects.get(name='init_failed')
            Instance.save()

        return super(CreateMissionView, self).form_valid(form)

class UpdateMissionView(UpdateView):
    template_name = u'mission_form.html'
    model = Mission
    form_class = forms.MissionForm
    success_url = reverse_lazy('mission')


    def get(self, request, *args, **kwargs):
        mark=kwargs['mark']
        self.object = Mission.objects.get(mark=mark)
        form = self.get_form(instance=self.object)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        mark=kwargs['mark']
        self.object = Mission.objects.get(mark=mark)
        form = self.get_form(data=request.POST, files=request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateMissionView, self).get_context_data(**kwargs)

        context['title'] = u'添加应用程序'

        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'

        # login partial and commons
        context['hello'] = u'欢迎回来, '
        context['login'] = u'登录'
        context['logout'] = u'注销'

        return context


class DeleteMissionView(DeleteView):
    success_url = reverse_lazy('mission')
    template_name='mission_confirm_delete.html'
    model = Mission
    form_class = forms.MissionForm

    def get(self, request, *args, **kwargs):
        mark=kwargs['mark']
        self.object = Mission.objects.get(mark=mark)
        form = self.get_form(instance=self.object)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        mark=kwargs['mark']
        self.object = Mission.objects.get(mark=mark)
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(DeleteMissionView, self).get_context_data(**kwargs)

        context['title'] = u'添加应用程序'

        context['btnsubmit'] = u'删除'
        context['btncancel'] = u'取消'

        # login partial and commons
        context['hello'] = u'欢迎回来, '
        context['login'] = u'登录'
        context['logout'] = u'注销'

        return context