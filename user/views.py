import traceback

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User

@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):
    def get(self,request,*args,**kwargs):
        uname=request.GET.get('username')
        print(uname)
        print('get请求')

        if uname:
            user = User.objects.filter(username=uname).values()
            if user:
                # return HttpResponse('get 请求')
                return JsonResponse({'status':200,'message':'查询单个用户成功','user':list(user)})
        else:
            users=User.objects.all().values()
            return JsonResponse({'status':200,'message':'查询所有用户成功','user':list(users)})
        return JsonResponse({'status': 500, 'message': '查询失败'})
    def post(self,request,*args,**kwargs):
        try:
            print('post请求')
            uname=request.POST.get('username')
            pwd=request.POST.get('password')
            age=request.POST.get('age')
            print(uname)
            with transaction.atomic():
                user=User.objects.create(username=uname,password=pwd,age=age)
                if user:
                    return JsonResponse({'status':'200',
                                         'message':'创建用户成功',
                                         'user':{'username':uname,'password':pwd,'age':age}})
                return HttpResponse({'status': 500, 'message': '创建用户失败'})
        except:
            traceback.print_exc()
    def put(self,request,*args,**kwargs):
        print('修改请求')
        return HttpResponse('修改 请求')
    def delete(self,request,*args,**kwargs):
        print('删除请求')
        return HttpResponse('删除 请求')
    def patch(self,request,*args,**kwargs):
        print('局部修改请求')
        return HttpResponse('局部修改 请求')

class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        re=request.GET
        # id = kwargs.get('id')
        # print(id)
        # if id:
        #     return Response({'status': 200, 'message': '查询id成功','id':id})
        # print(re['username'])
        # print(re)
        # print(list(re))
        # return Response('DRF_get请求')
        if re:
            uname = re['username']
            user = User.objects.filter(username=uname).values()
            if user:
                # return HttpResponse('get 请求')
                return Response({'status':200,'message':'查询单个用户成功','user':list(user)})
        else:
            users=User.objects.all().values()
            return Response({'status':200,'message':'查询所有用户成功','user':list(users)})
        return Response({'status': 500, 'message': '查询失败'})

    def post(self,request,*args,**kwargs):
        try:
            re = request.POST
            uname = re['username']
            pwd=re['password']
            age=re['age']
            print(uname,pwd,age)
            with transaction.atomic():
                user=User.objects.create(username=uname,password=pwd,age=age)
                if user:
                    return Response({'status':'200',
                                         'message':'创建用户成功',
                                         'user':{'username':uname,'password':pwd,'age':age}})
                return Response({'status': 500, 'message': '创建用户失败'})
        except:
            traceback.print_exc()

    def put(self,request,*args,**kwargs):
        print('修改请求')
        return Response('修改 请求')
    def delete(self,request,*args,**kwargs):
        print('删除请求')
        return Response('删除 请求')
    def patch(self,request,*args,**kwargs):
        print('局部修改请求')
        return Response('局部修改 请求')

