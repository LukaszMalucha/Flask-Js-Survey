from ma import ma
from marshmallow import pre_dump, fields
from models.user import UserModel


class UserSchema(ma.Schema):
    class Meta:
        # model = UserModel
        # confirm = fields.String()
        # load_only = ("password","confirm")  # not returnable fields, only to load
        # dump_only = ("id","confirmation")  # returnable only, not to load
        fields = ('username', 'email', 'password', 'confirm')


    # @pre_dump
    # def _pre_dump(self, user: UserModel):
    #     """get only the latest confirmation before json creation """
    #     user.confirmation = [user.most_recent_confirmation]
    #     return user
