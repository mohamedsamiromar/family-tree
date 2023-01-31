from family.models import Person
from customuser.models import User
from family import queries
from .models import (
    Father,
    Mather,
    GrandFather,
    GrandMother,
    GreatGrandFather,
    GreatGrandMother,
    Person,
    Wife,
    Husband
)


class PersonService:
    @staticmethod
    def create_user(
        first_name: str,
        middle_name: str,
        last_name: str
    ) -> User:
        user = User(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        user.save()
        return user


    @staticmethod
    def create_grand_father(
        user: dict = None,
        great_grand_father: dict = None,
        great_grand_mather: dict = None
    ):
        user = PersonService.create_user(**user)
        great_grand_father = PersonService.create_user(**great_grand_father)
        great_grand_mather = PersonService.create_user(**great_grand_mather)

        grand_farther = GrandFather(
            user=user,
            great_grand_father = great_grand_father,
            great_grand_mather = great_grand_mather
        )
        grand_farther.save()
        return grand_farther


        @staticmethod
        def create_grand_mather(
            
        ):
            pass



    @staticmethod
    def create_person(
            user: User,
            grand_father: dict = None,
            grand_mather: dict = None,
            father: dict = None,
            mather: dict = None,
            wife: dict = None,
            husband: dict = None,
            gender: dict = None
    ) -> Person:
        grand_father = PersonService.create_grand_father(**grand_father)

    