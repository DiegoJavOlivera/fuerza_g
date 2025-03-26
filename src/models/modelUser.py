from .entities.user import User
from models.dataBaseManager import DataBaseManager


class ModelUser:
    """
    ModelUser handles user authentication and management in the database.

    This class provides methods to manage user authentication, store temporary users, 
    move them to active users, update passwords, and check user existence in the system.

    Attributes:
    -------
        connection_db (DataBaseManager): An instance of the database manager 
                                         responsible for executing queries.
    """

    def __init__(self, connection_db: DataBaseManager):
        """
        Initializes the ModelUser instance with a database connection.

        Args:
            connection_db (DataBaseManager): An instance of the database manager
                                             responsible for executing queries.
        """
        self.connection_db = connection_db

    def login(self, user: User) -> tuple | None:
        """
        Authenticates a user by verifying the provided credentials.

        This method retrieves the user's hashed password from the database
        and compares it with the provided password using a secure hashing function.

        Args:
        ------
            user (User): An instance of the User class containing the login credentials.

        Returns:
        ------
            tuple | None: A tuple containing the user's data (id, email, password, name, 
                          last name, gender, payment service status) if authentication 
                          is successful, otherwise None.
        """
        q_sql = """SELECT id_user, email, password, name, lastName, gender, payment_service_status, admin  FROM user_lado_oscuro WHERE email = %s"""
        row = self.connection_db.execute_query(q_sql, (user.email,), fetchone=True)

        if row and user.check_password(row[2], user.password):
            return row

    def save_temp_user(self, user:User)-> None:
        """
        Saves a temporary user record into the 'lado_oscuro_usuarios_temporales' table in the database.

        This method hashes the user's password before saving it, and inserts essential details such as email, 
        name, last name, gender, and notification preference into the database.

        Args:
        -
            user (User): An instance of the User class containing the following attributes:
                - user.email (str): The user's email address.
                - user.password (str): The user's plain text password (which will be hashed before saving).
                - user.name (str): The user's first name.
                - user.last_name (str): The user's last name.
                - user.gender (str): The user's gender.
                - user.receive_not (bool): A flag indicating if the user wants to receive email notifications.

        Returns:
        -
            None: This method does not return any value, it performs an insert operation in the database.

        Raises:
        -
            Exception: If there is an error in the database connection or query execution, an exception will be raised.


        """
        
        q_sql = """INSERT INTO lado_oscuro_usuarios_temporales (id_user ,email, password , name ,lastName, gender, receive_email_notifications)
        VALUES (%s, %s, %s, %s, %s, %s ,%s)"""
        hashed_password = user.hash_password_generate(user.password)
        self.connection_db.execute_query(q_sql, (user.id, user.email, hashed_password, user.name, user.last_name, user.gender, user.receive_notification), commit=True)

    def move_to_active_user(self,email:str) -> bool:
        """
        Moves a confirmed temporary user to the 'user_lado_oscuro' table.

        This method retrieves the user's data from the 'lado_oscuro_usuarios_temporales' table and inserts it 
        into the 'user_lado_oscuro' table. After a successful transfer, it marks the user as confirmed 
        and removes them from the temporary users table.

        Args:
        -
            email (str): The email address of the user to be moved to the active users table.

        Returns:
        -
            bool: Returns `True` if the user was successfully moved, otherwise returns `False`.

        Raises:
        -
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """
        
        q_sql = """SELECT email, password, name, lastName, gender, receive_email_notifications FROM lado_oscuro_usuarios_temporales
        WHERE email = %s"""
        row = self.connection_db.execute_query(q_sql,(email,),fetchone=True)
        if row:
            q_sql = """INSERT INTO user_lado_oscuro (email, password, name, lastName, gender, receive_email_notifications) VALUES (%s, %s, %s ,%s ,%s, %s)"""
            self.connection_db.execute_query(q_sql,(row[0], row[1], row[2], row[3], row[4], row[5]),commit=True)
            self.confirm_active(email)
            self.remove_moved_temporal_user(email)
            return True
        
        return False

    def remove_moved_temporal_user(self,email:str) -> None:
        """
        Removes a temporary user from the 'lado_oscuro_usuarios_temporales' table if the confirmation status is TRUE.

        This method deletes a user record from the temporary users table based on the provided email address, 
        but only if the user has been confirmed.

        Args:
        -------
            email (str): The email address of the user to be removed.

        Returns:
        -------
            None: This method does not return any value; it executes a DELETE operation in the database.

        Raises:
        -------
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """
        q_sql = """DELETE  FROM lado_oscuro_usuarios_temporales WHERE confirm = TRUE and email = %s"""
        self.connection_db.execute_query(q_sql,(email,),commit=True)

    def confirm_active(self, email:str) -> None:
        """
        Marks a temporary user as confirmed in the 'lado_oscuro_usuarios_temporales' table.

        This method updates the confirmation status of a user by setting the 'confirm' field to TRUE.

        Args:
        -
            email (str): The email address of the user to be marked as confirmed.

        Returns:
        -
            None: This method does not return any value; it performs an UPDATE operation in the database.

        Raises:
        -
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """
        q_sql = """UPDATE lado_oscuro_usuarios_temporales
                SET confirm = TRUE
                WHERE email = %s"""
        self.connection_db.execute_query(q_sql, (email,),commit=True)
    
    def update_password(self, email: str, password: str) -> bool:
        """
        Updates the password for a user in the 'user_lado_oscuro' table.

        This method hashes the new password and updates the user's password in the database.

        Args:
        -
            email (str): The email address of the user whose password needs to be updated.
            password (str): The new password to set for the user.

        Returns:
        -
            bool: Returns `True` if the password was successfully updated, otherwise `False`.

        Raises:
        -
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """

        hashed_password = User.hash_password_generate(password)
        q_sql = """UPDATE user_lado_oscuro SET password = %s WHERE email = %s"""
        rows_affected = self.connection_db.execute_query(q_sql, (hashed_password, email), commit=True)

        return rows_affected > 0

    def email_exist(self, email:str) -> tuple | None:
        """
        Checks if an email exists in the 'user_lado_oscuro' table.

        This method verifies whether a given email address is already registered in the active users table.

        Args:
        -----
            email (str): The email address to check for existence.

        Returns:
        -----
            tuple | None:
                - Returns a tuple containing the email if it exists in the database.
                - Returns `None` if the email is not found.

        Raises:
        -----
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """
        q_sql = """SELECT email FROM user_lado_oscuro WHERE email = %s"""
        return self.connection_db.execute_query(q_sql,(email,),fetchone=True) 
  
    def email_exist_current_user(self, email: str)-> tuple | None:
        """
        Checks if a given email exists in the 'lado_oscuro_usuarios_temporales' table in the database.

        This method queries the database to determine if the specified email is already registered.

        Args:
        -----
            email (str): The email address to be verified.

        Returns:
        -----
            tuple | None:
                - A tuple containing the email if it exists in the database.
                - None if the email is not found.

        Raises:
        -----
            Exception: If there is an error in the database connection or query execution, an exception will be raised.
        """
        q_sql = """SELECT email from lado_oscuro_usuarios_temporales where email = %s"""
        return self.connection_db.execute_query(q_sql,(email,),fetchone=True)

    def get_by_id(self,id) -> User | None:
        """
        Retrieves a user from the 'user_lado_oscuro' table by their ID.

        This method executes a SQL query to fetch user data based on the given ID. 
        If a user is found, it returns an instance of the User class with the retrieved data. 
        The password is not included in the returned object for security reasons.

        Args:
        -
            id (int): The unique identifier of the user.

        Returns:
        -
            User | None: A User object if the user exists, otherwise None.
        """
        q_sql = """SELECT id_user, email, password, name, lastName, gender, payment_service_status, admin, receive_email_notifications FROM user_lado_oscuro 
        WHERE id_user = %s """
        row = self.connection_db.execute_query(q_sql,(id,),fetchone=True)
        if row:
            logged_user = User(row[0], row[1], None, row[3], row[4], row[5], row[6], row[7], row[8])
            return logged_user
        