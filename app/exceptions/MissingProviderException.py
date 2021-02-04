from exceptions.BaseException import ExceptionBase


class MissingProvider(ExceptionBase):
    def __init__(self, code=None, message=None):
        super().__init__(code=code, message=message)
