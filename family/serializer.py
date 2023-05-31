from rest_framework import serializers
from . models import  Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_day = serializers.CharField()
    death_date = serializers.CharField()
    family = serializers.CharField()


class MarriageRelationshipSerializer(serializers.Serializer):
    spouse_one = PersonSerializer()
    spouse_two = PersonSerializer()
    marriage_date = serializers.DateField()


class ParentChildRelationshipSerializer(serializers.Serializer):
    parent = serializers.IntegerField()
    child = PersonSerializer()


class FamilyTreeSerializer(serializers.Serializer):
    person = PersonSerializer()
    child = ParentChildRelationshipSerializer(required=False, many=True)
    marriage = MarriageRelationshipSerializer(required=False)


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
