from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage

class FileStorageField(fields.Field):
    """custom serializer field"""
    default_error_messages = {
        "invalid": "Not a valid image."

    }
    def _deserialize(self, value, attr, data):
        if value is None:
            return None

        if not isinstance(value, FileStorage):
            self.fail("invalid")
        return value

class ImageSchema(Schema):
    """gets the required  storage field, check if it exists and checks if it's a file storage"""
    image = FileStorageField(required=True)