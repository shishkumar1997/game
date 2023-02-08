from django.shortcuts import render
import requests
from requests import request
from rest_framework import generics,status
from rest_framework.permissions import IsAdminUser
from .models import Studentdetail
from rest_framework.response import Response
from .serializers import PostStudentSerializer,StudentSerializer
# Create your views here.

class StudentdetailAPI(generics.GenericAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        if request.method == 'GET':
            return StudentSerializer
        elif request.method == 'POST':
            return PostStudentSerializer
        return super().get_queryset()
    

    def get(self,request,id=None,*args, **kwargs):
        # try:

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
            context = {'status':True , 'message':"All student Information", 'data':serializer.data}
            return Response(context,status=status.HTTP_200_OK)
        # except Exception as e:
        #     # logger.error

    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {'status':True , 'message':"Craete student information successfully", 'data':serializer.data}
            return Response(context,status=status.HTTP_200_OK)
        context = {'status':True , 'message':"All student Information", 'data':serializer.errors}
        return Response(context,status=status.HTTP_200_OK)




