class ObjectResponse:
    def __init__(self, data={}):
        self.status = False
        self.cls_exception = None
        self.response = data
        self.users_phones = []
        self.__set_attr(self.response)

    def __getattr__(self, _):
        """
        Overriding the default behavior of not found exception
        """
        return None

    def __set_attr(self, data):
        self.fill_data(self, data)

    def set(self, key, value):
        if self.has_key(key):
            self.fill_data(self.get(key), value)
        else:
            setattr(self, key, ObjectResponse(value))

    def fill_data(self, obj, data):
        for key, value in data.items():
            if type(value) == dict:
                setattr(obj, key, ObjectResponse(value))
            else:
                setattr(obj, str(key), value)

    def get(self, key):
        return getattr(self, key)

    def has_key(self, key):
        _element = self
        key_path = key.split('.')

        for key in key_path:
            if _element and _element.get(key):
                _element = _element.get(key)
            else:
                return False

        return True

    def jsonify(self):
        attributes = self.__dict__
        primitives = (int, str, bool, list, dict, float)
        neglected_attributes = ["cls_exception", "response", "status"]
        json_data = dict()
        for k, v in attributes.items():
            if isinstance(v, ObjectResponse):
                json_data[k] = v.jsonify()
            elif (type(v) in primitives) and (k not in neglected_attributes):
                json_data[k] = v

        return json_data

    def get_response(self):
        if self.cls_exception:
            return self.cls_exception.get_response()
        else:
            if isinstance(self.response, ObjectResponse):
                return self.response.jsonify()
            return self.response
