from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,"index.html") #request为请求对象，index.html返回给客户端的页面
	
def login_action(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		#if username=='admin' and password=='admin123':
		user = auth.authenticate(username=username,password=password) #验证正确返回，否则返回None
		if user is not None:
				auth.login(request,user) 
				#response.set_cookie('user',username,3600) #添加浏览器cookie
				request.session['user']=username #将session记录保存到浏览器
				response = HttpResponseRedirect('/event_manage/') #重定向并作为返回
				return response
		else:
			return render(request,'index.html',{'error':'usernma or password error!'})


#发布会管理
@login_required
def event_manage(request):
	#username = request.COOKIES.get('user','') #读取浏览器cookie
	username = request.session.get('user','')#读取浏览器session
	return render(request,"event_manage.html",{"user":username})