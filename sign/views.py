from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,"index.html") #requestΪ�������index.html���ظ��ͻ��˵�ҳ��
	
def login_action(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		#if username=='admin' and password=='admin123':
		user = auth.authenticate(username=username,password=password) #��֤��ȷ���أ����򷵻�None
		if user is not None:
				auth.login(request,user) 
				#response.set_cookie('user',username,3600) #��������cookie
				request.session['user']=username #��session��¼���浽�����
				response = HttpResponseRedirect('/event_manage/') #�ض�����Ϊ����
				return response
		else:
			return render(request,'index.html',{'error':'usernma or password error!'})


#���������
@login_required
def event_manage(request):
	#username = request.COOKIES.get('user','') #��ȡ�����cookie
	username = request.session.get('user','')#��ȡ�����session
	return render(request,"event_manage.html",{"user":username})