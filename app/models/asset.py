from . import BaseModel, TenantMixin
from ..extensions import db

class Asset(BaseModel, TenantMixin):
    __tablename__ = 'assets'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    status = db.Column(db.String(20))

    def __repr__(self):
        return f'<Asset {self.name}>'