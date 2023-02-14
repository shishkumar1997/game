from rest_framework import serializers
from .models import Studentdetail

#get student serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        fields = '__all__'

#post student serializer
class AddStudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # image = serializers.ImageField()
    # username = serializers.EmailField(required=True)

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
        
        stuobj = Studentdetail.objects.filter(username__iexact=username).first()
        if stuobj:
            raise serializers.ValidationError({'error':'User is already register.'})
        if first_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        if middle_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        if last_name.isdigit():
            raise serializers.ValidationError({'error':'Please enter only alphabates'})
        return super().validate(attrs)
#show post student serializer

class ShowAddStudentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    # image = serializers.ImageField()
    # username = serializers.EmailField(required=False)

    class Meta:
        model = Studentdetail
        fields = '__all__'
        fields = ['id','name','username',"is_deleted",'image','created_on','updated_on']
    
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