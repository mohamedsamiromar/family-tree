from typing import Dict, Optional

from django.db import transaction

from core.errors import APIError, Error
from .models import (
    Person,
    Family,
    ParentChildRelationship,
    MarriageRelationship
)


class FamilyService:

    @staticmethod
    def family_service(
            person: Dict,
            child: Optional[Dict] = None,
            marriage: Optional[Dict] = None
    ) -> Person:
        with transaction.atomic():
            try:
                person = Person(**person)
                person.save()
                family = Family(surname=person.get('family'))
                family.save()
            except:
                transaction.rollback
                raise APIError(Error.PERSON_CREATION_FAILED)
        return person