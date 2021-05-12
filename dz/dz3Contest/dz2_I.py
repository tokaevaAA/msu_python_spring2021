import copy


class FragileDict:
    def __init__(self, d=None):
        if (d is None):
            d = {}
        self._data = copy.deepcopy(d)
        self._lock = True

    def __enter__(self):
        self.tmp_dict = copy.deepcopy(dict())
        self._lock = False
        return self

    def __contains__(self, key):
        if (hasattr(self, 'tmp_dict')):
            if (key in self._data or key in self.tmp_dict):
                return True
            else:
                return False
        else:
            return key in self._data

    def __getitem__(self, key):
        if (hasattr(self, 'tmp_dict')):
            if (key not in self._data and key not in self.tmp_dict):
                raise KeyError(key)
            if (key in self.tmp_dict):
                return self.tmp_dict[key]
            elif (key in self._data):
                self.tmp_dict[key] = copy.deepcopy(self._data[key])
                return self.tmp_dict[key]
        else:
            if (key not in self._data):
                raise KeyError(key)
            if (self._lock is True):
                return copy.deepcopy(self._data[key])
            else:
                setattr(self, 'tmp_dict', copy.deepcopy(dict()))
                self.tmp_dict[key] = copy.deepcopy(self._data[key])
                return self.tmp_dict[key]

    def __setitem__(self, key, val):
        if (self._lock is True):
            raise RuntimeError("Protected state")
        if (hasattr(self, 'tmp_dict')):
            if (key not in self.tmp_dict):
                self.tmp_dict[key] = copy.deepcopy(val)
        else:
            setattr(self, 'tmp_dict', copy.deepcopy(dict()))
            self.tmp_dict[key] = copy.deepcopy(self._data[key])

    def __exit__(self, exc_type, exc_value, traceback):
        if (exc_type is None):
            if (hasattr(self, 'tmp_dict')):
                self._data.update(copy.deepcopy(self.tmp_dict))
                delattr(self, 'tmp_dict')
        else:
            print("Exception has been suppressed.")
            if (hasattr(self, 'tmp_dict')):
                delattr(self, 'tmp_dict')
        self._lock = True
        return True
