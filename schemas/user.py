from ma import ma
from marshmallow import pre_dump
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)  # not returnable fields, only to load
        dump_only = ("id","confirmation")  # returnable only, not to load
        fields = ('username', 'email', 'password', 'confirm', 'remember')



    @pre_dump
    def _pre_dump(self, user: UserModel):
        """get only the latest confirmation before json creation """
        user.confirmation = [user.most_recent_confirmation]
        return user
