from family.models import Person
from customuser.models import User
from family import queries
from .models import *


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
        print("############")
