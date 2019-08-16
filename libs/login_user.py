from flask_login import LoginManager, login_user, logout_user, AnonymousUserMixin


login_manager = LoginManager()




@login_manager.user_loader
def load_user(user_id):
    return UserModel.find_by_id(int(user_id))


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.email = 'Guest'


login_manager.anonymous_user = Anonymous