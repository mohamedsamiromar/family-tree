from .models import Father, Mather, Wife, Husband
from customuser.models import User
from core.errors import APIError, Error


def get_user(user: int) -> User:
    try:
        return User.objects.get(id=user)
    except User.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
            User._meta.model_name
        ])


def get_father(father: int) -> Father:
    try:
        return Father.objects.get(pk=father)
    except Father.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
            Father._meta.model_name
        ])


def get_mather(mather: int) -> Mather:
    try:
        return Mather.objects.get(pk=mather)
    except Father.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
            Mather._meta.model_name])


def get_wife(wife: int) -> Wife:
    try:
        return Wife.objects.get(pk=wife)
    except Wife.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
            Wife._meta.model_name
        ])


def get_husband(husband: int) -> Husband:
    try:
        return Husband.objects.get(pk=husband)
    except Husband.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
            Husband._meta.model_name
        ])
