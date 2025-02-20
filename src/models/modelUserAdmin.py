from models.dataBaseManager import DataBaseManager
from models.entities.exams import Exams
from models.entities.news import News


class ModelUserAdmin:

    def __init__(self, connection_db: DataBaseManager):
        self.connection_db = connection_db
    
    def save_news(self, news: News) -> bool:
        """
        Saves a new news article to the database.

        This method inserts the provided news details into the `news` table in the database.
        The information includes the date, title, content, and an image associated with the article.

        Args:
        ------
            news (News): An instance of the News class containing the details of the news article.
                        It should have the attributes: `date`, `title`, `content`, and `image`.

        Returns:
        ------
            bool: True if one or more rows were successfully inserted into the database, otherwise False.
                The method returns a boolean indicating whether the insertion affected at least one row.
        """
        q_sql = """INSERT INTO news (date, title, content, image) VALUES (%s, %s, %s, %s)"""
        result = self.connection_db.execute_query(q_sql, (news.date, news.title, news.content, news.image),commit=True)
        return result > 0
        
    

    def save_subject_exam(self, exams: Exams) -> bool:
        """
        Saves a new exam for a subject to the database.

        This method inserts the provided exam details into the `subject_utn` table in the database.
        The information includes the title, image, date, content, and the associated subject of the exam.

        Args:
        ------
            exams (Exams): An instance of the Exams class containing the details of the exam.
                            It should have the attributes: `title`, `image_exam`, `date`, `content`, and `subject`.

        Returns:
        ------
            bool: True if one or more rows were successfully inserted into the database, otherwise False.
                The method returns a boolean indicating whether the insertion affected at least one row.
        """
        q_sql = """INSERT INTO subject_utn (title, imagen_exam, date, content, subject) VALUES (%s, %s, %s, %s, %s)"""
        result = self.connection_db.execute_query(q_sql, (exams.title, exams.image_exam, exams.date, exams.content, exams.subject),commit=True)
        return result > 0


    
        
