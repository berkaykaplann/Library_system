class User:
    id_counter = 1

    def __init__(self, name, email, user_type="member", id=None):
        if id is None:
            self.id = str(User.id_counter)
            User.id_counter += 1
        else:
            self.id = str(id)
        self.name = name
        self.email = email
        self.user_type = user_type

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "user_type": self.user_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            email=data["email"],
            user_type=data["user_type"],
            id=data["id"]
        )
