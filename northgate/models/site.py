from yaml import safe_load
from uuid import uuid8

from .models import BaseModel

class Site(BaseModel):
    """
    Represents a site with various attributes such as name, visibility, local status,
    password, entry point, allowed extensions, and description.
    Inherits from BaseModel.
    """
    database_table = "sites"

    def __init__(self, id, name, visibility, path, local=False, password=None, entry=None, allowed_extensions=None, description=None):
        id = id if id is not None else str(uuid8())
        self.id = id if isinstance(id, str) else str(id)
        self.name = name
        self.visibility = visibility
        self.path = path
        self.local = local
        self.password = password
        self.entry = entry
        self.allowed_extensions = allowed_extensions if allowed_extensions is not None else []
        self.description = description

    def fields(self):
        return ["id", "name", "visibility", "path", "local", "password", "entry", "allowed_extensions", "description"]
    
    def toJson(self):
        return super().toJson()
    
    @staticmethod
    def fromYaml(id, path, yaml_data):
        if isinstance(yaml_data, str):
            yaml_data = safe_load(yaml_data)
        return Site(
            id=id,
            name=yaml_data.get("name"),
            visibility=yaml_data.get("visibility"),
            path=path,
            local=yaml_data.get("local", False),
            password=yaml_data.get("password"),
            entry=yaml_data.get("entry"),
            allowed_extensions=yaml_data.get("allowed_extensions"),
            description=yaml_data.get("description")
        )
