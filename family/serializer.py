from rest_framework import serializers
from .models import Person, Father, Mather, GrandFather, GrandMother, \
    GreatGrandFather, GreatGrandMother
from customuser.models import User


class CreatePersonSerializer(serializers.Serializer):
    father = serializers.IntegerField(write_only=True, required=True)
    mather = serializers.IntegerField(write_only=True, required=True)
    gender = serializers.CharField(write_only=True, required=True)
    wife = serializers.IntegerField(
        write_only=True, required=False, allow_null=True)
    husband = serializers.IntegerField(
        write_only=True, allow_null=True
    )


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
