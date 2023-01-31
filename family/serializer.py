from rest_framework import serializers
from .models import Person, Father, Mather
from customuser.models import User


class UserInformationSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True, required=True)
    middle_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)


class GreatGrandFatherForFatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()


class GreatGrandMatherForFatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()


class GrandFatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()
    great_grand_father = GreatGrandFatherForFatherSerializer()
    great_grand_mather = GreatGrandMatherForFatherSerializer()


class GreatGrandFatherForMatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()


class GreatGrandMatherForMatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()


class GrandMatherSerializer(serializers.Serializer):
    user = UserInformationSerializer()
    great_grand_father = GreatGrandFatherForMatherSerializer()
    great_grand_mather = GreatGrandMatherForMatherSerializer()


class CreatePersonSerializer(serializers.Serializer):
    grand_father = GrandFatherSerializer(required=True, write_only=True)
    grand_mather = GrandMatherSerializer(required=True, write_only=True)
    father = UserInformationSerializer(required=True, write_only=True)
    mather = UserInformationSerializer(required=True, write_only=True)
    wife = UserInformationSerializer(required=False, allow_null=True, write_only=True)
    husband = UserInformationSerializer(required=False, allow_null=True, write_only=True)
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
