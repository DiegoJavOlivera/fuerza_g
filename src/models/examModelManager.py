from models.dataBaseManager import DataBaseManager


class ExamModelManager:
    """
    Manages exam-related database operations for the 'subject_utn' table.

    This class provides methods to retrieve exam records based on subject or exam ID.

    Attributes:
    -----
        connection_db (DataBaseManager): The database connection manager instance used to execute queries.
    """
    def __init__(self, connection_db:DataBaseManager ):
        self.connection_db = connection_db

     
    def get_all_exams(self, subject: str) -> tuple | None:
        """
        Retrieves all exam records from the 'subject_utn' table for a given subject, ordered by date in descending order.

        Args:
        -----
            subject (str): The subject name to filter exams.

        Returns:
        -----
            tuple | None:
                - A tuple containing all exam records for the specified subject.
                - None if no exams are found.

        Raises:
        -----
            Exception: If an error occurs while executing the query.
        """
        
        q_sql = """SELECT * FROM subject_utn WHERE subject = %s ORDER BY date DESC"""
        return self.connection_db.execute_query(q_sql,(subject,))
        

    
    def get_one_exam(self, id_exam: int) -> tuple | None:
        """
        Retrieves a single exam record from the 'subject_utn' table based on the provided exam ID.

        Args:
        -----
            id_exam (int): The ID of the exam to retrieve.

        Returns:
        -----
            tuple | None:
                - A tuple containing the exam data if found.
                - None if no exam is found with the given ID.

        Raises:
        -----
            Exception: If an error occurs while executing the query.
        """
        q_sql = """SELECT * FROM subject_utn WHERE id_subject = %s"""
        return self.connection_db.execute_query(q_sql,(id_exam,),fetchone=True)
        