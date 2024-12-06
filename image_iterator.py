import os
from PIL import Image

class ImageIterator:
    def __init__(self, folder_path):
        """
        Инициализирует `ImageIterator`, сохраняя путь к папке, находя все файлы изображений в этой папке и устанавливая начальный индекс для итерации
        param folder_path: Строка, содержащая путь к папке с изображениями
        """
        self.folder_path = folder_path
        self.image_files = [
            f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Метод для получения следующего изображения.
        Return: Путь к следующему изображению.
        """
        if self.index >= len(self.image_files):
            raise StopIteration
        image_path = os.path.join(self.folder_path, self.image_files[self.index])
        self.index += 1
        return image_path
