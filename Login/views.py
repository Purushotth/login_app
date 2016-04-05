from django.shortcuts import render, render_to_response, redirect
from django.http import *

from django import template

from django.template import RequestContext, loader

from django.views.generic import View


import forms

from Login.models import LoginModel
# Create your views here.

class LoginForm(View):
	Credentials = True

	def Loggedin(self,request):
		return False if 'status' in request.get_full_path() else True

	def get(self, request):
		form =  forms.LoginForm()
		Loggedin = self.Loggedin(request)
		return render_to_response('login.html',{'form':form,'Credentials':self.Credentials, 'Loggedin': Loggedin},context_instance = RequestContext(request))

	def post(self, request,*args,**kwargs):
		print dir(request),str(request),args,kwargs
		form = 	forms.LoginForm(request.POST)
                Loggedin = self.Loggedin(request)
		if form.is_valid():
			Last_Name = form.cleaned_data['Last_Name']
			EmailID = form.cleaned_data['EmailID']
			SSN = form.cleaned_data['SSN']
			try:
				uid = LoginModel.objects.get(Last_Name = Last_Name, EmailID = EmailID, SSN = SSN).uid
				request.session[uid] = True
	                        return HttpResponseRedirect('/{uid}/'.format(uid = uid))
			except LoginModel.DoesNotExist:
				self.Credentials = False

		return render_to_response('login.html',{'form':forms.LoginForm(),'Credentials':self.Credentials,'Loggedin': Loggedin},context_instance = RequestContext(request))

class LoginPage(View):
        Credentials = True
	Loggedin = True

	def getuid(self, request):
		return request.get_full_path().strip('/')

	def get(self,request):
                uid = self.getuid(request)
		if not request.session.has_key(uid):
			return HttpResponseRedirect('/login/?status=/logout/')

		Last_Name = LoginModel.objects.get(uid = uid).Last_Name
                EmailID = LoginModel.objects.get(uid = uid).EmailID
                SSN = LoginModel.objects.get(uid = uid).SSN

                return render_to_response('out-table.html',{'Last_Name': Last_Name,'EmailID':EmailID,'SSN':SSN},context_instance = RequestContext(request))

        def post(self,request):
                uid = self.getuid(request)
                if request.session.has_key(uid):
			del request.session[uid]
		return HttpResponseRedirect('/login/')

