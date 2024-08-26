from . import BaseModel
from ..extensions import db

class Tenant(BaseModel):
    __tablename__ = 'tenants'

    name = db.Column(db.String(100), nullable=False)
    schema_name = db.Column(db.String(63), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tenant {self.name}>'