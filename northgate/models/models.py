import json
from abc import abstractmethod

class BaseModel:
    def __init__(self):
        pass

    @abstractmethod
    def fields(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def toDict(self):
        dict = {}
        for field in self.fields():
            dict[field] = getattr(self, field, None)
        return dict
    
    def toJson(self):
        return json.dumps(self.toDict())
