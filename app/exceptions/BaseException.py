from abc import ABC


class ExceptionBase(ABC):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def set_status_code(self, code):
        self.code = code

    def set_content(self, message):
        self.message = message

    def get_response(self):
        return {"status_code": self.code, "message": self.message}
