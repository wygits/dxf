from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    sid = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,max_length=100)
    sex = serializers.ChoiceField(choices=[('man','男'),('woman','女')],default='man')
    datadate = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sid = validated_data.get('sid',instance.sid)
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.datadate = validated_data.get('datadate', instance.datadate)
        instance.save()
        return instance

