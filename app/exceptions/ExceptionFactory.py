from utils.common import FAILED_CONNECTION_EXCEPTION, UN_KNOWN_EXCEPTION, BAD_REQUEST_EXCEPTION, \
    MISSING_PROVIDER_EXCEPTION, VALIDATION_EXCEPTION
from exceptions.BadRequestException import BadRequest
from exceptions.MissingProviderException import MissingProvider
from exceptions.FailedConnectionException import FailedConnection
from exceptions.UnknownException import UnknownException
from exceptions.ValidationException import Validation


class ExceptionFactory:
    mapper_dict = {
        BAD_REQUEST_EXCEPTION: BadRequest,
        MISSING_PROVIDER_EXCEPTION: MissingProvider,
        FAILED_CONNECTION_EXCEPTION: FailedConnection,
        UN_KNOWN_EXCEPTION: UnknownException,
        VALIDATION_EXCEPTION: Validation,
    }

    @staticmethod
    def get_exception(exception_cls_name, status_code, message):
        if not ExceptionFactory.mapper_dict.get(exception_cls_name):
            return ExceptionFactory.mapper_dict[UN_KNOWN_EXCEPTION](status_code, message)
        return ExceptionFactory.mapper_dict[exception_cls_name](status_code, message)
