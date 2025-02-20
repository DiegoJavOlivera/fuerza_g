from models.dataBaseManager import DataBaseManager

class NewsManager:
    """
    Manages operations related to news records in the database.

    Attributes:
    -----
        connection_db (DataBaseManager): 
            An instance of DataBaseManager used to interact with the database.
    """
    def __init__(self, connection_db: DataBaseManager):
        """
        Initializes the NewsManager with a database query executor.

        Args:
        -----
            connection_db (DataBaseManager): 
                The database query manager responsible for executing SQL operations.
        """
        self.connection_db = connection_db


    
    def get_all_news(self)-> list[tuple] | None:
        """
        Retrieves all news records from the 'news' table, ordered by date in descending order.

        Returns:
        -----
            list[tuple] | None:
                - A list of tuples, where each tuple represents a news record.
                - None if no news records are found.

        Raises:
        -----
            Exception: If an error occurs while executing the query.
        """
        q_sql = """SELECT * FROM news ORDER BY date DESC """
        return self.connection_db.execute_query(q_sql)
        
    
    def get_one_news(self,id_news: int)-> tuple | None:
        """
        Retrieves a single news record from the 'news' table based on the provided news ID.

        Args:
        -----
            id_news (int): The ID of the news article to retrieve.

        Returns:
        -----
            tuple | None:
                - A tuple containing the news data if found.
                - None if no news record is found with the given ID.

        Raises:
        -----
            Exception: If an error occurs while executing the query.
        """
        q_sql = """SELECT * FROM news WHERE id_news = %s"""
        return self.connection_db.execute_query(q_sql,(id_news,),fetchone=True)
        