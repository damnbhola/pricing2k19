import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.model import Model
from common.utils import Utils
import models.user.errors as UserErrors


@dataclass(eq=False)
class User(Model):
    collection: str = field(init=False, default="users")
    name: str
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)

        if not Utils.check_password(password, user.password):
            raise UserErrors.IncorrectPasswordError("Your  password is incorrect!")

        return True

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        found = cls.find_one_by("email", email)
        if found is None:
            raise UserErrors.UserNotFoundError("A  user with this e-mail was not found!")
        return found

    @classmethod
    def register_user(cls, name: str, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The  e-mail does not have a right format!")

        try:
            cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError("The  e-mail you used already exists!")
        except UserErrors.UserNotFoundError:
            User(name, email, password).save_to_mongo()

        return True
