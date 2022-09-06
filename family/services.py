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


class PersonService:

    @staticmethod
    def create_person(
            gender: str,
            great_grand_father_for_father: dict,
            great_grand_mather_for_father: dict,
            great_grand_father_for_mather: dict,
            great_grand_mather_for_mather: dict,
            grand_father: dict,
            grand_mather: dict,
            father: dict,
            mather: dict,
            wife: dict = None,
            husband: dict = None
    ) -> Person:
        # Great Grand Father
        user_information_great_grand_father = UserInformationService.creat_user_information(
            first_name=great_grand_father_for_father['first_name'],
            middle_name=great_grand_father_for_father['middle_name'],
            last_name=great_grand_father_for_father['last_name'],
        )

        user_information_great_grand_mather = UserInformationService.creat_user_information(
            first_name=great_grand_mather_for_father['first_name'],
            middle_name=great_grand_mather_for_father['middle_name'],
            last_name=great_grand_mather_for_father['last_name'],
        )

        create_great_grand_father = GreatGrandFather(
            user=user_information_great_grand_father
        )
        create_great_grand_father.save()

        create_great_grand_mather = GreatGrandMother(
            user=user_information_great_grand_mather)
        create_great_grand_mather.save()

        # Grand Father
        user_information_grand_father = UserInformationService.creat_user_information(
            first_name=grand_father['first_name'],
            middle_name=grand_father['middle_name'],
            last_name=grand_father['last_name'],
        )

        create_grand_father = GrandFather(
            user=user_information_grand_father,
            great_grand_father=create_great_grand_father,
            great_grand_mather=create_great_grand_mather
        )
        create_grand_father.save()
