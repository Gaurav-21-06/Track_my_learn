from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, user_data):

        self.id = user_data["id"]
        self.full_name = user_data["full_name"]
        self.email = user_data["email"]
        self.password = user_data["password"]
        self.is_verified = user_data["is_verified"]

    def get_id(self):
        return str(self.id)