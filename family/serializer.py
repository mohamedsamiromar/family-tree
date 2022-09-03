from rest_framework import serializers
from .models import Person, Father, Mather, GrandFather, GrandMother, \
    GreatGrandFather, GreatGrandMother
from customuser.models import User


class CreatePersonSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    birth_day = serializers.DateField(write_only=True)
    father = serializers.IntegerField(write_only=True)
    mather = serializers.IntegerField(write_only=True)
    gender = serializers.CharField()
    wife = serializers.IntegerField(required=False, allow_null=False)
    husband = serializers.IntegerField(required=False, allow_null=False)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='full_name')

    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'birth_date',
        ]


class GrandMatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandMother
        fields = []


class GrandFatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandFather
        fields = 1


class ListPersonRelativesSerializer(serializers.ModelSerializer):
    class FatherSerializer(serializers.ModelSerializer):
        user = UserSerializer()

        class Meta:
            model = Father
            fields = [
                'user'
            ]

    father = FatherSerializer()

    class Meta:
        model = Person
        fields = [
            'user',
            'father'
        ]
