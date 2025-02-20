from models.dataBaseManager import DataBaseManager
from flask import current_app
from flask_mail import Message, Mail
import os

class EmailService:
    
    def __init__(self, connection_db:DataBaseManager, mail: Mail):
        """
        Service class for handling email operations using Flask-Mail.

        Attributes:
        -----------
        connection_db (DataBaseManager):
            The database manager instance used for executing queries.
        mail (Mail):
            The Flask-Mail instance used for sending emails.
        """
        self.connection_db = connection_db
        self.mail = mail

    def get_all_users_receive_not(self) -> list[tuple]| None:
        """
        Retrieves the email addresses of all users who have opted to receive email notifications.

        Returns:
        -----
            list[tuple] | None:
                - A list of tuples, where each tuple contains a single email address.
                - None if no users are found.

        Raises:
        -----
            Exception: If an error occurs while executing the query.
        """
        q_sql = """SELECT email FROM user_lado_oscuro WHERE receive_email_notifications = %s"""
        return self.connection_db.execute_query(q_sql,(True,))
    
    def sends_emails(self, content : str, emails:list[tuple]|str, title="", mass_send=False)-> None:
        """
        Sends an email or multiple emails using the configured mail service.

        This method allows sending individual emails or bulk emails, depending on the 'mass_send' parameter.
        If 'mass_send' is True, it iterates over the list of email recipients and sends an email to each.
        Otherwise, it sends a single email.

        Args:
        -----
            content (str): 
                The body of the email. It must be a string containing either plain text or HTML content.
            emails (list | str): 
                - If 'mass_send' is True, this should be a list of tuples where each tuple contains an email address.
                - If 'mass_send' is False, this should be a single email address as a string.
            title (str, optional): 
                The subject of the email. Defaults to an empty string.
            mass_send (bool, optional): 
                Determines whether the method sends a bulk email (True) or a single email (False). Defaults to False.

        Raises:
        ------
            Exception: If an error occurs while sending the email, an exception is raised with a descriptive message.
        """
        try:    
            with current_app.app_context():
                if mass_send:    
                    for email in emails:
                        msg = Message(title, recipients=[email[0]], sender=os.getenv("MAIL_DEFAULT_SENDER"))
                        msg.html = content
                        self.mail.send(msg)
                        
                else:
                    msg = Message(title, recipients= [emails], sender= os.getenv("MAIL_DEFAULT_SENDER"))
                    msg.html = content
                    self.mail.send(msg)                                               

        except Exception as e:
                raise Exception(f"Error al enviar un email: {e}")
