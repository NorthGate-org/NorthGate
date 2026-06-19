from yaml import safe_load

from .models import BaseModel

class Site(BaseModel):
    """
    Represents a site with various attributes such as name, visibility, local status,
    password, entry point, allowed extensions, and description.
    Inherits from BaseModel.
    """
    database_table = "sites"

    def __init__(self, name, visibility, local=False, password=None, entry=None, allowed_extensions=None, description=None):
        self.name = name
        self.visibility = visibility
        self.local = local
        self.password = password
        self.entry = entry
        self.allowed_extensions = allowed_extensions if allowed_extensions is not None else []
        self.description = description

    def fields(self):
        return ["name", "visibility", "local", "password", "entry", "allowed_extensions", "description"]
    
    def toJson(self):
        return super().toJson()
    
    @staticmethod
    def fromYaml(yaml_data):
        if isinstance(yaml_data, str):
            yaml_data = safe_load(yaml_data)
        return Site(
            name=yaml_data.get("name"),
            visibility=yaml_data.get("visibility"),
            local=yaml_data.get("local", False),
            password=yaml_data.get("password"),
            entry=yaml_data.get("entry"),
            allowed_extensions=yaml_data.get("allowed_extensions"),
            description=yaml_data.get("description")
        )
