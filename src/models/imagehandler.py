import os
from werkzeug.utils import secure_filename


class ImageHandler:
    """
    This class is responsible for handling image uploads and saving them to the
    server.
    """

    def save_news_image(self, news_image) -> str:
        """
        Saves a news image to the server and returns the path where it was saved.
        args:
            news_image (FileStorage): The image file to save.
        returns:
            str: The path where the image was saved.
        """
        filename = secure_filename(news_image.filename)
        image_path = os.path.join(os.getenv("UPLOAD_FOLDER"), filename)
        news_image.save(image_path)
        return os.path.join(os.getenv("FOLDER_IMG"), filename).replace("\\", "/")
    
    def save_exam_image(self,exam_image) -> str:
        """
        Saves a exam image to the server and returns the path where it was saved.
        args:
            exam_image (FileStorage): The image file to save.
        returns:
            str: The path where the image was saved.
        """
        filename = secure_filename(exam_image.filename)
        image_exam_path = os.path.join(os.getenv("UPLOAD_FOLDER_EXAM"),filename)
        exam_image.save(image_exam_path)
        return os.path.join(os.getenv("FOLDER_IMG_EXAM"), filename).replace("\\","/")