import uuid

from db import db
from sqlalchemy_utils import UUIDType


class TagModel(db.Model):
    __tablename__ = "tag"

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    package = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(500))
    created_on = db.Column(db.BigInteger, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    updated_on = db.Column(db.BigInteger)
    updated_by = db.Column(db.String(50))
