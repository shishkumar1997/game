from django.shortcuts import render
import requests
from requests import request
from rest_framework import generics,status
from rest_framework.permissions import *
from .models import Studentdetail
from rest_framework.response import Response
from .serializers import AddStudentSerializer,StudentSerializer,UpdateStudentSerializer,Update1StudentSerializer,ShowAddStudentSerializer,LoginStudentSerializer,Login1StudentSerializer,ShowLoginStudentSerializer
import xlwt
from xlwt import Workbook
from django.contrib.auth.hashers import make_password,check_password
# from .tests import generate_access_token,generate_refresh_token
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from .tests import generate_access_token,generate_refresh_token
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import xlsxwriter
import pandas as pd
# class kamal(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         return Response({'msg':'Hello'})

class StudentdetailAPI(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]

    serializer_class = StudentSerializer
    swagger_user_id = openapi.Parameter('user_id',in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[swagger_user_id])
    def get(self,request):
        try:
            user_id = self.request.query_params.get('user_id', None)
            if user_id:
                print('--------------------11111111111111111111111')
                Student_data = Studentdetail.objects.filter(id=user_id,is_deleted=False).last()
                serializer = self.serializer_class(Student_data,many=False)
                print('--------------------222222')
                # convert into dataframe
                df = pd.DataFrame(data=serializer.data, index=[1])
                #convert into excel
                df.to_excel("students121.xlsx", index=False)
                context = {'status':True , 'message':"All student Information", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)

            Student_data = Studentdetail.objects.filter(is_deleted=False).all()
            serializer = self.serializer_class(Student_data,many=True)
            # convert into dataframe
            df = pd.DataFrame(data=serializer.data)
            #convert into excel
            df.to_excel("students123.xlsx", index=False)
            
            context = {'status':True , 'message':"All student Information", 'data':serializer.data}
            return Response(context,status=status.HTTP_200_OK)
        except Exception as e:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request,*args, **kwargs):
        try:
            serializer = AddStudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {'status':True , 'message':"Craete student information successfully", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.conf import settings
from django.core.mail import send_mail
class AddStudentdetailAPI(generics.GenericAPIView):
    serializer_class = AddStudentSerializer
    def post(self,request,*args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                mkdir=serializer.save()
                serializer_data=ShowAddStudentSerializer(mkdir)
                Studentdetail.objects.filter(username__iexact=serializer_data.data.get('username')).update(password=make_password(request.data.get('password')),email=(request.data.get('username')))

                subject = 'welcome to GFG world'
                message = f'Hi, thank you for registering in geeksforgeeks.'
                email_from = 'ashishk140@triazinesoft.com'
                recipient_list = ['ashishk140@triazinesoft.com', ]
                send_mail( subject, message, email_from, recipient_list )
                context = {'status':True , 'message':"Craete student information successfully", 'data':serializer_data.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class UpdateStudentdetailAPI(generics.GenericAPIView):
    serializer_class = UpdateStudentSerializer

    def put(self,request,*args, **kwargs):
        try:
            student_id = request.data.get('student_id',None)
            if not student_id:
                context = {'status':False , 'message':"Enter valid key of student id"}
                return Response(context,status=status.HTTP_200_OK)
            studentobj = Studentdetail.objects.filter(id=student_id).first()
            if not studentobj:
                context = {'status':False , 'message':"Please enter valid student id"}
                return Response(context,status=status.HTTP_200_OK)    
            serializer = self.serializer_class(studentobj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {'status':True , 'message':"Update student information successfully", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Update1StudentdetailAPI(generics.GenericAPIView):
    serializer_class = Update1StudentSerializer

    def put(self,request,*args, **kwargs):
        try:
            # student_id = context.get('') 
            # print(request.data)
            # print(request.data.get('id'),'====data')

            serializer = self.serializer_class(request.data.get('id'), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                context = {'status':True , 'message':"Update student information successfully", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

import datetime
#delete Student detail
class DeleteStudentdetailAPI(generics.GenericAPIView):

    def delete(self,request,*args, **kwargs):
        try:
            stu = request.GET.get('student_id',None)
            stuobj = Studentdetail.objects.filter(id=stu).first()
            if not stuobj:
                context = {'status':False , 'message':"Student data is not exits."}
                return Response(context,status=status.HTTP_200_OK)
            if stuobj.is_deleted==True:
                context = {'status':True , 'message':"Student data already delete Success."}
                return Response(context,status=status.HTTP_200_OK)
            Studentdetail.objects.filter(id=stuobj.id).update(is_deleted=True,updated_on=datetime.datetime.now())
            context = {'status':True , 'message':"Student data delete successfully"}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Schedule Library imported
# import schedule
# import time

# # Functions setup
# def sudo_placement():
# 	print("Get ready for Sudo Placement at ashish")

# def good_luck():
# 	print("Good Luck for Test")

# def work():
# 	print("Study and work hard")

# def bedtime():
# 	print("It is bed time go rest")
	
# def geeks():
# 	print("Shaurya says ashish")

# # Task scheduling
# # After every 10mins geeks() is called.
# schedule.every(10).minutes.do(geeks)

# # After every hour geeks() is called.
# schedule.every().hour.do(geeks)

# # Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(bedtime)

# # After every 5 to 10mins in between run work()
# schedule.every(5).to(10).minutes.do(work)

# # Every monday good_luck() is called
# schedule.every().monday.do(good_luck)

# # Every tuesday at 18:00 sudo_placement() is called
# schedule.every().tuesday.at("18:00").do(sudo_placement)

# # Loop so that the scheduling task
# # keeps on running all time.
# while True:

# 	# Checks whether a scheduled task
# 	# is pending to run or not
# 	schedule.run_pending()
# 	time.sleep(1)

# feedback/views.py

# from .forms import FeedbackForm
# from django.views.generic.edit import FormView
# from django.views.generic.base import TemplateView

# class FeedbackFormView(FormView):
#     template_name = "feedback/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/success/"

#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)

# class SuccessView(TemplateView):
#     template_name = "feedback/success.html"


#Student login api
class StudentLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginStudentSerializer

    def post(self,request,*args, **kwargs):

        try:
            stuobj = Studentdetail.objects.filter(username__iexact=request.data.get('username')).first()
            if not stuobj:
                context = {'status':True , 'message':"Please enter valid username."}
                return Response(context,status=status.HTTP_200_OK)
            serializer = ShowLoginStudentSerializer(stuobj,many=False)
            if serializer:
                password_validation=check_password(request.data.get('password'),stuobj.password)

                if not password_validation:
                    context = {'status':True , 'message':"Password is not match."}
                    return Response(context,status=status.HTTP_200_OK) 
                access_token = generate_access_token(stuobj.id)
                context = {'status':True , 'message':"Login student information successfully.",'access_token':access_token, 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def AddEmployee(request):
    if request.method == 'POST':
        serializer = AddStudentSerializer(data=request.data)
        if serializer.is_valid():
            gg=serializer.save()
            serializer_data = ShowAddStudentSerializer(gg)
            context = {'status':True , 'message':"Craete student information successfully", 'data':serializer_data.data}
            return render(request,'account/index.html',context)
    serializer = AddStudentSerializer()
    context = {'status':True , 'message':"Craete student information successfully", 'data':serializer_data.data}
    return render(request,'account/index.html',context)
        

def ListStudent(request):
    if request.method == 'GET':
        studata=Studentdetail.objects.all()
        serializer = StudentSerializer(studata, many=True)
        context = {'data':serializer.data}
        # data=serializer.data
        # for i in 
        # context = {'status':True , 'message':"Craete student information successfully", 'data':serializer.data}
        return render(request,'account/list.html',context)
    serializer = StudentSerializer()
    context = {'status':True , 'message':"Craete student information successfully", 'data':serializer.data}
    return render(request,'account/list.html',context) 
