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
    Husband,
    UserInformation
)

class PersonService():

    def create_user_info(self, first_name: str, middle_name: str, last_name: str) -> UserInformation:
        user = UserInformation(
            first_name = first_name, middle_name = middle_name, last_name= last_name
        )
        user.save()
        return user

    def create_great_grand_father(self, user) -> GreatGrandFather:
        user = self.create_user_info(**user)
        great_grand_father = GreatGrandFather(user=user).save
        return great_grand_father

    def create_great_grand_mather(self, user) -> GreatGrandMother:
        user = self.create_user_info(**user)
        great_grand_mather = GreatGrandMother(user=user).save
        return great_grand_mather

    def create_grand_father(self, user: dict, great_grand_father: dict, great_grand_mather: dict) -> GrandFather:
        user = self.create_user_info(**user)
        great_grand_father = self.create_great_grand_father(**great_grand_father)
        great_grand_mather = self.create_great_grand_mather(**great_grand_mather)
        grand_father = GrandFather(
            user=user,
            great_grand_father = great_grand_father,
            great_grand_mather = great_grand_mather
        ).save()
        return grand_father

    def create_grand_mather(self, user: dict, great_grand_father: dict, great_grand_mather: dict) -> GrandMother:
        user = self.create_user_info(**user)
        great_grand_father = self.create_great_grand_father(**great_grand_father)
        great_grand_mather = self.create_great_grand_mather(**great_grand_mather)
        grand_father = GrandMother(
            user=user,
            great_grand_father = great_grand_father,
            great_grand_mather = great_grand_mather
        ).save()
        return grand_father


    def create_father(self, user: dict, grand_father: dict, grand_mather: dict) -> Father:
        user = self.create_user_info(**user)
        grand_father = self.create_grand_father(**grand_father)
        grand_mather = self.create_grand_mather(**grand_mather)
        father = Father(
            user=user,
            grand_father=grand_father,
            grand_mather=grand_mather
        ).save()
        return father


    def create_mather(self, user: dict, grand_father: dict, grand_mather: dict) -> Mather:
        user = self.create_user_info(**user)
        grand_father = self.create_grand_father(**grand_father)
        grand_mather = self.create_grand_mather(**grand_mather)
        mather = Mather(
            user=user,
            grand_father=grand_father,
            grand_mather=grand_mather
        ).save()
        return mather

    def create_wife(self, user: dict, father: dict, mather: dict) -> Wife:
        user = self.create_user_info(**user)
        father = self.create_father(**father)
        mather = self.create_mather(**mather)
        wife = Wife(
            user = user,
            father = father,
            mather=mather
        ).save()
        return wife

    def create_husband(self, user: dict, father: dict, mather: dict) -> Husband:
        user = self.create_user_info(**user)
        father = self.create_father(**father)
        mather = self.create_mather(**mather)
        husband = Husband(
            user = user,
            father = father,
            mather=mather
        ).save()
        return husband

    def create_person( self, user: User, father: dict, mather: dict,  gender: str, wife: dict = None, husband: dict = None ) -> Person:
        father = self.create_father(**father) 
        mather = self.create_mather(**mather)
        wife = self.create_wife(**wife)
        husband = self.create_husband(**husband)
        person = Person(
            user = user,
            father = father,
            mather = mather,
            wife = wife,
            husband = husband,
            gender = gender
        ).save()
        return person