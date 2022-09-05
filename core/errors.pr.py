from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum
import logging

logger = logging.getLogger('django')


class Error(Enum):
    DEFAULT = {"code": -000, "detail": _("Oops!. Something went wrong, please contact us")}
    INSTANCE = {"code": 404, "detail": _("not found!")}


class APIError:
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger.info(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
