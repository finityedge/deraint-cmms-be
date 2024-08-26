from ..extensions import db

class TenantMixin:
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

from .tenant import Tenant
from .asset import Asset
# Import other models here