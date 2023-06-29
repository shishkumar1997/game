from amqp import Message
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework import status,generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import UserSerializer
from .models import*
# Create your views here.

# class SignupUser(generics.GenericAPIView):
serializer_class=UserSerializer
def UserView(request):
    if request.method=="POST":
        serializer = UserSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('api/signup/')
        return render(request, 'authapp/index.html')
            # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            # return redirect('/api/signup/')
            # return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # serializer_class = UserSerializer
    
    # def get(self,request,*args, **kwargs):
    #     # try:
    #         user_id = request.data.get('user_id',None)
    #         if user_id:
    #             print('=========================',user_id)
    #             userobj = User.objects.filter(id=user_id).first()
    #             serializer = self.serializer_class(userobj,many=False)
    #             context = {status:True,'message':"User record create successfully",'data':serializer.data}
    #             return render(request,'authapp/index.html',{'form':serializer.data})
    #             # return Response(context,status=status.HTTP_200_OK)
    #         print('=====@@@@@@@@@@@@@@@@@@@@2')
    #         userobj = User.objects.all()
    #         print(userobj,'===')
    #         serializer = UserSerializer(userobj,many=True)
    #         print(serializer.data,'=====SER')
    #         context = {'status':True,'message':"User record create successfully",'data':serializer.data}
    #         # return Response(context,status=status.HTTP_200_OK)
    #         return render(request,'authapp/index.html',{'form':serializer.data})
    #     # except:
    #     #     context = {status:False,'message':"Something Went Wrong"}
    #     #     return Response(context,status=status.HTTP_200_OK)

# from django.conf import settings
    # from django.contrib import messages
    # def post(self,request,*args, **kwargs):
    #     # try:
    #         serializer = self.serializer_class(data=request.data)
    #         print(serializer,'111111111111111111')
    #         if serializer.is_valid():
    #             serializer.save()
    #             context = {status:True,'message':"User record create successfully"}
    #             print('88888888888888888888888888888888888888888888888888')
    #             return redirect('/api/signup/')
    #         print('22222222222222222222222222222222')
    #         context = {status:False,'message':serializer.error}
    #         return Response(context,status=status.HTTP_200_OK)
        # except:
        #     context = {status:False,'message':"Something Went Wrong"}
        #     return Response(context,status=status.HTTP_200_OK)

            

