from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum
import logging

logger = logging.getLogger('django')


class Error(Enum):
    DEFAULT = {"code": -000, "detail": _("Oops!. Something went wrong, please contact us")}
    INSTANCE_NOT_FOUND = {"code": 404, "detail": _("{} not found!")}
    BLOCKED_USER = {'code': -403, 'detail': _('User is banned!')}
    NO_ACTIVE_ACCOUNT = {'code': -500, 'detail': _('No active account found with the given credentials!')}
    PERSON_CREATION_FAILED = {'code': -500, 'detail': _('No active account found with the given credentials!')}


class APIError(Exception):
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in formatting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger.warning(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
