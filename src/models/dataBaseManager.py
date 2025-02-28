from flask import current_app


class DataBaseManager:


    def __init__(self, db_connection, schema_file):
        """
        The constructor must receive the database object to execute queries from its methods.

        Args:
            db_connection (object): The database connection object used for executing queries.
            schema_file (str): The path to the SQL file containing the database schema.
        """
        self.db_connection = db_connection
        self.schema_file = schema_file

    def execute_query(self,query: str, params=(), commit=False, fetchone=False, fetchvalue=False):
        """
        Executes an SQL query on the connected database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple, optional): Parameters to include in the SQL query for prepared statements. Defaults to an empty tuple ().
            commit (bool, optional): Whether to commit the transaction after executing the query. Defaults to False.
            fetchone (bool, optional): Whether to fetch only a single result row. Defaults to False.
            fetchvalue (bool, optional): Whether to fetch a single scalar value from the result (e.g., the first column of the first row). Defaults to False.

        Raises:
            Exception: If an error occurs while executing the query, an exception is raised with details.

        Returns:
            Any: 
                - If `fetchone` is True, returns a single row as a tuple or None if no rows are found.
                - If `fetchvalue` is True, returns a single value or None if no rows are found.
                - If the query is a `SELECT` query and neither `fetchone` nor `fetchvalue` is True, returns all rows as a list of tuples.
                - If the query is not a `SELECT` query, returns the number of rows affected.
        """
        try:
            with self.db_connection.connection.cursor() as cursor:
                cursor.execute(query, params)
                if commit:
                    self.db_connection.connection.commit()
                if query.strip().lower().startswith("select"):
                    if fetchone:
                        return cursor.fetchone()
                    elif fetchvalue:
                        row = cursor.fetchone()
                        return row[0] if row else None
                    else:
                        return cursor.fetchall()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(f"Error ejecutando la consulta {ex}")
        
    def initialize_database(self):
        """
        Initializes the database by executing the SQL statements in the schema file.
        """
        if not self.is_database_initialized():
            try:
                with open(self.schema_file, "r", encoding="utf-8") as file:
                    schema_sql = file.read()

                for statement in schema_sql.split(";"):
                    if statement.strip():
                        self.execute_query(statement, commit=True)
            except Exception as ex:
                raise Exception(f"Error inicializando la base de datos {ex}")
        

    def is_database_initialized(self):
        """
        Checks if the database has been initialized by verifying the existence of required tables.

        Returns:
            bool: True if the required tables exist, False otherwise.
        """
        try:
            result = self.execute_query("SHOW TABLES", fetchone=True)

            return bool(result)
        except Exception:
            return False
    