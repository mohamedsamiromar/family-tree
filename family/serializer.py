from rest_framework import serializers
from .models import Person, Father, Mather, GrandFather, GrandMother, \
    GreatGrandFather, GreatGrandMother
from customuser.models import User


class UserInformationSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True)
    middle_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)


class GreatGrandFatherForFatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()


class GreatGrandMatherForFatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()


class GrandFatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()
    great_grand_father = GreatGrandFatherForFatherSerializer()
    great_grand_mather = GreatGrandMatherForFatherSerializer()


class GreatGrandFatherForMatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()


class GreatGrandMatherForMatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()

class GrandMatherSerializer(serializers.Serializer):
    user_information = UserInformationSerializer()
    great_grand_father = GreatGrandFatherForMatherSerializer()
    great_grand_mather = GreatGrandMatherForMatherSerializer()


class CreatePersonSerializer(serializers.Serializer):
    grand_father = GrandFatherSerializer(required=True)
    grand_mather = GrandMatherSerializer(required=True)
    father = UserInformationSerializer(required=True)
    mather = UserInformationSerializer(required=True)
    wife = UserInformationSerializer(required=False, allow_null=True)
    husband = UserInformationSerializer(required=False, allow_null=True)
    gender = serializers.CharField(
        write_only=True, required=False, allow_null=True)


class PersonSerializer(serializers.ModelSerializer):
    # Father Serializer
    class FatherSerializer(serializers.ModelSerializer):
        full_name = serializers.SerializerMethodField()

        class Meta:
            model = Father
            fields = ["full_name", "grand_father", "grand_mather"]

        def get_full_name(self, obj):
            return obj.user.full_name

    # Mother Serializer
    class MatherSerializer(serializers.ModelSerializer):
        full_name = serializers.SerializerMethodField()

        class Meta:
            model = Mather
            fields = ["full_name", "grand_father", "grand_mather"]

        def get_full_name(self, obj):
            return obj.user.full_name

    full_name = serializers.SerializerMethodField()
    father = FatherSerializer()
    mather = MatherSerializer()

    class Meta:
        model = Person
        fields = [
            "full_name",
            "father",
            "mather",
            "gender",
            "wife",
            "husband"
        ]

    def get_full_name(self, obj):
        return obj.user.full_name
