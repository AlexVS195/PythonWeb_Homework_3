import os
import shutil

# Функція для сортування файлів за розширенням у папці
def sort_files_by_extension(folder):
    file_extension_mapping = {}
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            if extension not in file_extension_mapping:
                file_extension_mapping[extension] = []
            file_extension_mapping[extension].append(file_path)
    return file_extension_mapping

# Функція для переміщення файлів у папку за розширенням
def move_files(destination_folder, file_list):
    for file in file_list:
        shutil.move(file, destination_folder)

if __name__ == "__main__":
    try:
        # Отримання шляху до папки для сортування від користувача
        folder = input("Введіть шлях до папки для сортування: ")
        # Перевіряємо, чи існує вказана папка
        if not os.path.exists(folder):
            raise FileNotFoundError("Папка не існує!")
        
        # Сортуємо файли у папці "Хлам" та отримуємо відображення розширень файлів
        file_extension_mapping = sort_files_by_extension(folder)
        
        # Переміщуємо файли в окремі папки за їхніми розширеннями
        for extension, files in file_extension_mapping.items():
            destination_folder = os.path.join(folder, extension[1:])  # Видаляємо крапку з розширення
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            move_files(destination_folder, files)

        print("Сортування завершено.")
    except FileNotFoundError as e:
        print(e)

