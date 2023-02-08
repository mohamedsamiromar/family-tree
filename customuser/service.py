from customuser.models import User, LoginLog
from core.errors import Error, APIError
from . models import GroupEnum


class AccountService:

    @staticmethod
    def optain_person_access_token(user: User, token: dict) -> dict:
        # if not user.groups.filter(name=GroupEnum.PERSON.value).exists():
        #     raise APIError(Error.NO_ACTIVE_ACCOUNT)
        token['roles'] = list(user.groups.all().values())
        return token

    @staticmethod
    def optain_access_token(group: GroupEnum, user: User, token: dict) -> dict:
        # if group == GroupEnum.PERSON:
        return AccountService.optain_person_access_token(
            user=user, token=token)
        # else:
        #     raise APIError(Error.NO_ACTIVE_ACCOUNT)

    @staticmethod
    def login(email: str) -> None:
        LoginLog.objects.create(email=email)