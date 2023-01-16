import time

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import TagModel
from schemas import TagSchema, TagUpdateSchema

from db import db

blp = Blueprint("tag", __name__, description="Tag API")


@blp.route("/tag/<string:id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, id):
        tag = TagModel.query.get_or_404(id)
        return tag

    @blp.arguments(TagUpdateSchema)
    @blp.response(200, TagSchema)
    def put(self, data, id):
        tag = TagModel.query.get(id)
        if tag:
            tag.package = data["package"]
            tag.version = data["version"]
            tag.name = data["name"]
            tag.updated_by = "barney"
            tag.updated_on = time.time_ns() // 1000000
        else:
            tag = TagModel(id=id, **data)
            tag.created_by = "barney"
            tag.created_on = time.time_ns() // 1000000
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while saving the tag")
        return tag

    def delete(self, id):
        tag = TagModel.query.get_or_404(id)
        try:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Item deleted."}
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting the tag")


@blp.route("/tag")
class TagList(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self):
        return TagModel.query.all()

    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, data):
        tag = TagModel(**data)
        tag.created_by = "fred"
        tag.created_on = time.time_ns() // 1000000
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while saving the tag")

        return tag


@blp.route("/search")
class TagSearch(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self):
        return TagModel.query.all()
