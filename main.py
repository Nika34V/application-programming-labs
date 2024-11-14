import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def load_image(input_path: str) -> np.ndarray:
    """
    Функция принимает путь к файлу изображения и возвращает изображение
    :param input_path: Строка, содержащая путь к файлу изображения
    :return: Изображение 
    """
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Ошибка: изображение не загружено.")
    return image

def display_image_info(image: np.ndarray) -> None:
    """
    Выводит информацию о размере изображения
    :param image: Многомерный массив NumPy, представляющий изображение.
    """
    if image is not None:
        print(f"Размер изображения: {image.shape}")
    else:
        print("Ошибка: изображение не загружено.")

def plot_histogram(image: np.ndarray) -> None:
    """
    Строит и отображает гистограмму интенсивностей пикселей
    :param image: Многомерный массив NumPy, представляющий изображение в оттенках серого
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.hist(image.ravel(), 256, [0, 256], color='gray')
        plt.title("Гистограмма изображения")
        plt.xlabel("Интенсивность пикселей")
        plt.ylabel("Количество пикселей")
        plt.show()
    except Exception as e:
        print(f"Ошибка при построении гистограммы: {e}")

def binarize_image(image: np.ndarray, threshold: int) -> np.ndarray:
    """
    Бинаризует изображение с заданным порогом
    :param image: Массив NumPy, представляющий изображение в оттенках серого.
           threshold: Целочисленное значение порога для бинаризации
    :return: Бинаризованное изображение
    """
    if image is None:
        raise ValueError("Ошибка: изображение не загружено.")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

def display_images(original: np.ndarray, binary: np.ndarray) -> None:
    """
    Отображает исходное и бинарное изображения
    :param original: Массив NumPy, представляющий исходное изображение в оттенках серого.
        binary: Массив NumPy, представляющий бинаризованное изображение
    """
    if original is None or binary is None:
        raise ValueError("Ошибка: одно из изображений не загружено.")
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Исходное изображение")
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.imshow(binary, cmap='gray')
    plt.title("Бинарное изображение")
    plt.axis("off")
    
    plt.show()

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Сохраняет изображение в файл
    :param image: Массив NumPy, представляющий изображение, которое нужно сохранить.
           output_path: Строка, представляющая путь к файлу, куда нужно сохранить изображение.
    """
    if not output_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValueError("Ошибка: укажите корректное расширение файла для сохранения (.jpg, .jpeg или .png).")
    if cv2.imwrite(output_path, image):
        print(f"Изображение сохранено по пути: {output_path}")
    else:
        raise IOError("Ошибка при сохранении изображения. Проверьте путь и разрешения на запись.")

def main(input_path: str, output_path: str, threshold: int = 127) -> None:
    """
    Основная функция для выполнения всех операций
    :param input_path: Строка, представляющая путь к файлу изображения, которое нужно обработать.
           output_path: Строка, представляющая путь к файлу, куда нужно сохранить бинаризованное изображение.
           threshold: Целое число, задающее пороговое значение для бинаризации.
    """
    image = load_image(input_path)
    display_image_info(image)
    plot_histogram(image)
    binary_image = binarize_image(image, threshold)
    display_images(image, binary_image)
    save_image(binary_image, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Обработка изображения и конвертация в бинарный формат.")
    parser.add_argument("input_path", type=str, help="Путь к исходному изображению")
    parser.add_argument("output_path", type=str, help="Путь для сохранения бинарного изображения")
    parser.add_argument("--threshold", type=int, default=127, help="Пороговое значение для бинаризации (по умолчанию: 127)")
    args = parser.parse_args()
    
    main(args.input_path, args.output_path, args.threshold)
