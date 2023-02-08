from rest_framework import serializers
from .models import Studentdetail

#get student serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        fields = '__all__'

#post student serializer
class PostStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentdetail
        fields = '__all__'
        fields = ['name']

    def validate(self, attrs):
        name = self.attrs.get('name')
        if name.is_digit():
            raise serializers.ValidationError('please enter alphabates')
        return super().validate(attrs)