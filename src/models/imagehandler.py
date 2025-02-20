import os
from werkzeug.utils import secure_filename


class ImageHandler:


    def save_news_image(self, news_image) -> str:
        filename = secure_filename(news_image.filename)
        image_path = os.path.join(os.getenv("UPLOAD_FOLDER"), filename)
        news_image.save(image_path)
        return os.path.join(os.getenv("FOLDER_IMG"), filename).replace("\\", "/")
    
    def save_exam_image(self,exam_image) -> str:
        filename = secure_filename(exam_image.filename)
        image_exam_path = os.path.join(os.getenv("UPLOAD_FOLDER_EXAM"),filename)
        exam_image.save(image_exam_path)
        return os.path.join(os.getenv("FOLDER_IMG_EXAM"), filename).replace("\\","/")