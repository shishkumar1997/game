from rest_framework import serializers

from account.utils import get_tokens_for_user
from .models import Studentdetail
from django.contrib.auth.hashers import make_password,check_password
# from .tests import generate_access_token,generate_refresh_token

def password_validation(password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if len(password) < 8:
            print("Password is at least 8 charactor.")
            # raise serializers.ValidationError({'error':'Please enter password at least 8 character'})
        if not mat:
            print("Password is valid.")
            # raise serializers.ValidationError({'error':'Password is valid.'})
        return mat
#get student serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        fields = '__all__'

import re 
#post student serializer
class AddStudentSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField()
    # image = serializers.ImageField()
    # username = serializers.CharField(required=False)

    class Meta:
        model = Studentdetail
        fields = '__all__'
        fields = ['id','first_name','middle_name','last_name','username','email','password',"is_deleted",'image','created_on','updated_on']

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        middle_name = attrs.get('middle_name')
        last_name = attrs.get('last_name')
        username = attrs.get('username')
        password = attrs.get('password')
        # password = make_password( attrs.get('password'))
        

        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        # reg = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        # pat = re.compile(reg)
        # mat = re.search(pat, password)
        mat = re.findall(reg, password)
        print(password,"aaaaaaaaaaaaaa444444444444444444")
        print(mat,'=============*******************************************')
        if len(password) < 8:
            raise serializers.ValidationError({'error':'Please enter password at least 8 character'})
        if not mat:
            raise serializers.ValidationError({'error':'Password is not valid.'})


        stuobj = Studentdetail.objects.filter(username__iexact=username).first()
        if stuobj:
            raise serializers.ValidationError({'error':'User is already register.'})
        if first_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        if middle_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        if last_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        print(attrs,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return super().validate(attrs)

#show post student serializer
class ShowAddStudentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    # image = serializers.ImageField()
    # username = serializers.EmailField(required=False)

    class Meta:
        model = Studentdetail
        fields = '__all__'
        fields = ['id','name','first_name','middle_name','last_name','username','email','password',"is_deleted",'image','created_on','updated_on']
    
    def get_name(self,obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}"

#update serializer
class UpdateStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        fields = '__all__'
        # fields = ['id','first_name','middle_name','last_name','username',"is_deleted",'image','created_on','updated_on']

    def validate(self, attrs):
        name = attrs.get('name')
        # name = attrs.get('name')

        # if name.isdigit():
        #     raise serializers.ValidationError({'error':'Please enter only alphabates'})
        # return super().validate(attrs)
    
#update1 serializer
class Update1StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()

    class Meta:
        model = Studentdetail
        fields = '__all__'
        # fields = ['id','first_name','middle_name','last_name','username',"is_deleted",'image','created_on','updated_on']

    def validate(self, attrs):
        id = attrs.get('id')
        # name = attrs.get('name')

        studentobj = Studentdetail.objects.filter(id=id).first()
        dd= Studentdetail.objects.all()
        if not studentobj:
            raise serializers.ValidationError({'error':'Please enter valid student id'})
        # if name.isdigit():
        #     raise serializers.ValidationError({'error':'Please enter only alphabates'})
        # return super().validate(attrs)

#login student serializer
class LoginStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        # fields = '__all__'
        fields = ['username','password']
#showlogin student serializer
class ShowLoginStudentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    tokens = serializers.SerializerMethodField()
    # refresh_token = serializers.SerializerMethodField()

    class Meta:
        model = Studentdetail
        # fields = '__all__'
        fields = ['tokens','id','name','first_name','middle_name','last_name','username','password',"is_deleted",'image','created_on','updated_on']

    def get_name(self,obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}"

    def get_tokens(self,obj):
        print(obj,'jjjjjjjjjjjjjj')
        return get_tokens_for_user(obj)

    # def get_refresh_token(self,obj):
    #     return generate_refresh_token(obj.id)

# #login student serializer
# class LoginStudentSerializer(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField()
#     access_token = serializers.SerializerMethodField()
#     refresh_token = serializers.SerializerMethodField()

#     class Meta:
#         model = Studentdetail
#         # fields = '__all__'
#         fields = ['access_token','refresh_token','id','name','first_name','middle_name','last_name','username','password',"is_deleted",'image','created_on','updated_on']

#     def get_name(self,obj):
#         return f"{obj.first_name} {obj.middle_name} {obj.last_name}"

#     def get_access_token(self,obj):
#         return get_tokens_access_for_user(obj.id)

#     def get_refresh_token(self,obj):
#         return get_tokens_for_user(obj.id)

#login1 student serializer
class Login1StudentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Studentdetail
        # fields = '__all__'
        fields = ['id','name','first_name','middle_name','last_name','username','password',"is_deleted",'image','created_on','updated_on']

    def get_name(self,obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}"
    def validate(self, attrs):
        username = attrs.get('username',None)
        password = attrs.get('password',None)

        studentobj = Studentdetail.objects.filter(username__iexact=username).first()
        if not studentobj:
            raise serializers.ValidationError({'error':'Please enter valid username'})
        print(studentobj.password)
        print(password)
        # if check_password(studentobj.password,password):
        if not studentobj.password==password:
            raise serializers.ValidationError({'error':'Please enter valid password'})

        return super().validate(attrs)