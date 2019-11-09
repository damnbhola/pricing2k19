import re


class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.search("[a-z][a-z.,0-9]+@[a-z]+.[a-z]+", email)
        found_email = email_address_matcher.group(0)
        if email == found_email:
            return True
        return False

    @staticmethod
    def check_password(password: str, user_password: str) -> bool:
        return password == user_password
