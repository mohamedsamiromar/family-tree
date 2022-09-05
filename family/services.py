from family.models import Person
from customuser.models import User
from family import queries


class PersonService:

    @staticmethod
    def create_person(
            user: User,
            father: int,
            mather: int,
            gender: str,
            wife: int = None,
            husband: int = None
    ) -> Person:
        get_father = queries.get_father(father=father)
        get_mather = queries.get_mather(mather=mather)

        person = Person(
            user=user,
            father=get_father,
            mather=get_mather,
            gender=gender
        )

        if wife:
            get_wife = queries.get_wife(wife=wife)
            person.wife = get_wife
        if husband:
            get_husband = queries.get_husband(husband=husband)
            person.husband = get_husband
        person.save()
        return person
