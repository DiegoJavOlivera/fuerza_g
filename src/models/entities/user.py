from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    

    def __init__(self, id, email, password, name = "", last_name = "", gender = "" ,payment_service_status = False, admin = False, receive_notification = False) -> None:
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.payment_service_status = payment_service_status
        self.admin = admin
        self.receive_notification = receive_notification

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)
    @classmethod
    def hash_password_generate(cls, password):
        return generate_password_hash(password)
    
    @classmethod
    def check_password_repeat(cls, password, repeat_password):
        return password == repeat_password
    
    @classmethod
    def check_google_mail(cls, email: str) -> bool:
        """
        Checks whether the given email belongs to Google's mail service (Gmail).

        This method verifies if the email domain is either 'gmail.com' or 'gmail.com.ar'.

        Args:
        -----
            email (str): 
                The email address to be checked.

        Returns:
        ------
            bool: 
                Returns `True` if the email belongs to Gmail, otherwise returns `False`.

        Raises:
        ------
            IndexError: 
                If the email format is invalid and does not contain '@'.
        """

        mail = email.split("@")
        return mail[1] == "gmail.com" or mail[1] == "gmail.com.ar"