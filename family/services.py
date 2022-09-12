from family.models import Person
from customuser.models import User
from family import queries
from .models import *


class UserInformationService:
    @staticmethod
    def creat_user_information(
            first_name: str,
            middle_name: str,
            last_name: str,
    ) -> UserInformation:
        create_user_information = UserInformation.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        return create_user_information

    @staticmethod
    def creat_grand_father(
            user_information: dict,
            great_grand_father: dict,
            great_grand_mather: dict
    ) -> GrandFather:
        grand_father_information = UserInformation.objects.create(
            first_name=user_information["first_name"],
            middle_name=user_information["middle_name"],
            last_name=user_information["last_name"]
        )
        user_great_grand_father_information = UserInformation.objects.create(
            first_name=great_grand_father["first_name"],
            middle_name=great_grand_father["middle_name"],
            last_name=great_grand_father["last_name"]
        )
        user_great_grand_mather_information = UserInformation.objects.create(
            first_name=great_grand_mather["first_name"],
            middle_name=great_grand_mather["middle_name"],
            last_name=great_grand_mather["last_name"]
        )
        grand_father = GrandFather.objects.create(
            user=grand_father_information,
            great_grand_father=user_great_grand_father_information,
            great_grand_mather=user_great_grand_mather_information
        )
        return grand_father

    @staticmethod
    def creat_grand_mather(
            user_information: dict,
            great_grand_father: dict,
            great_grand_mather: dict
    ) -> GrandFather:
        grand_mather_information = UserInformation.objects.create(
            first_name=user_information["first_name"],
            middle_name=user_information["middle_name"],
            last_name=user_information["last_name"]
        )
        user_great_grand_father_information = UserInformation.objects.create(
            first_name=great_grand_father["first_name"],
            middle_name=great_grand_father["middle_name"],
            last_name=great_grand_father["last_name"]
        )
        user_great_grand_mather_information = UserInformation.objects.create(
            first_name=great_grand_mather["first_name"],
            middle_name=great_grand_mather["middle_name"],
            last_name=great_grand_mather["last_name"]
        )
        grand_father = GrandMother.objects.create(
            user=grand_mather_information,
            great_grand_father=user_great_grand_father_information,
            great_grand_mather=user_great_grand_mather_information
        )
        return grand_father


class PersonService:

    @staticmethod
    def create_person(
            user: User,
            gender: str,
            grand_father: dict,
            grand_mather: dict,
            father: dict,
            mather: dict,
            wife: dict = None,
            husband: dict = None
    ) -> Person:
        pass
