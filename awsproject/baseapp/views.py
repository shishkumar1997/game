from django.shortcuts import render
import requests
from requests import request
from rest_framework import generics,status
from rest_framework.permissions import IsAdminUser
from .models import Studentdetail
from rest_framework.response import Response
from .serializers import AddStudentSerializer,StudentSerializer,UpdateStudentSerializer,Update1StudentSerializer,ShowAddStudentSerializer
import xlwt
from xlwt import Workbook
# Create your views here.

class StudentdetailAPI(generics.GenericAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        if request.method == 'GET':
            return StudentSerializer
        elif request.method == 'POST':
            return AddStudentSerializer
        return super().get_queryset()
    

    def get(self,request,id=None,*args, **kwargs):
        try:

            if id:
                Student_data = Studentdetail.objects.filter(id=id,is_deleted=False).first()
                if not Student_data:
                    context = {'status':False , 'message':"please enter valid id"}
                    return Response(context,status=status.HTTP_200_OK)
                serializer = self.serializer_class(Student_data)
                context = {'status':True , 'message':"All student Information", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)

            Student_data = Studentdetail.objects.filter(is_deleted=False).all()
            serializer = self.serializer_class(Student_data,many=True)
            #################

            
            # Workbook is created
            wb = Workbook()
            
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Sheet 1')
            
            sheet1.write(0, 0, 'id')
            sheet1.write(0, 1, 'name')
            sheet1.write(0, 2, 'is_deleted')
            sheet1.write(0, 3, 'image')
            for i in serializer.data:
                wb.save('xlwt example.xls')
            ##############
            context = {'status':True , 'message':"All student Information", 'data':serializer.data}
            return Response(context,status=status.HTTP_200_OK)
        except Exception as e:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request,*args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {'status':True , 'message':"Craete student information successfully", 'data':serializer.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        except:
            context = {'status':False , 'message':"Something went wrong"}
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddStudentdetailAPI(generics.GenericAPIView):
    serializer_class = AddStudentSerializer

    def post(self,request,*args, **kwargs):
        # try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                mkdir=serializer.save()
                serializer_data=ShowAddStudentSerializer(mkdir)
                context = {'status':True , 'message':"Craete student information successfully", 'data':serializer_data.data}
                return Response(context,status=status.HTTP_200_OK)
            context = {'status':False , 'message':"All student Information", 'data':serializer.errors}
            return Response(context,status=status.HTTP_200_OK)
        # except:
        #     context = {'status':False , 'message':"Something went wrong"}
        #     return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
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
            print(request.data)
            print(request.data.get('id'),'====data')

            serializer = self.serializer_class(request.data.get('id'), data=request.data, partial=True )
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

from .forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = "feedback/success.html"