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
    
    def insert_statement(self):
        if isinstance(self.allowed_extensions, list):
            self.allowed_extensions = ",".join(self.allowed_extensions)
        return (
            "INSERT INTO {} (id, name, visibility, path, local, password, entry, allowed_extensions, description) " \
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)".format(self.database_table),
            (self.id, self.name, self.visibility, self.path, self.local, self.password, self.entry, self.allowed_extensions, 
             self.description)
        )
    
    def update_statement(self):
        if isinstance(self.allowed_extensions, list):
            self.allowed_extensions = ",".join(self.allowed_extensions)
        return (
            "UPDATE {} SET name = ?, visibility = ?, path = ?, local = ?, password = ?, entry = ?, allowed_extensions = ?, " \
            "description = ? WHERE id = ?".format(self.database_table),
            (self.name, self.visibility, self.path, self.local, self.password, self.entry, self.allowed_extensions, 
             self.description, self.id)
        )
    
    def toDict(self):
        return super().toDict()
    
    def toJson(self):
        return super().toJson()
    
    @staticmethod
    def fromRow(row):
        return Site(
            id=row[0],
            name=row[1],
            visibility=row[2],
            path=row[3],
            local=row[4],
            password=row[5],
            entry=row[6],
            allowed_extensions=row[7],
            description=row[8]
        )
    
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
