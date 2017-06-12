class DummyClassDict:
    def __init__(self,inp_dict={}):
        self._dict = inp_dict
    def __dir__(self):
        return self._dict.keys()
    def __setitem__(self,key,item):
        self._dict[key] = item
    def __getitem__(self,key):
        return self._dict[key]
    def __getattr__(self,key):
        return self._dict[key]
    def __call__(self):
        return self._dict

