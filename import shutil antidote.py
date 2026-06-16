import shutil
from pathlib import Path

def undo_sorting(target_directory):
    target_dir = Path(target_directory)
    
    # Список папок, которые создал предыдущий скрипт
    created_folders = ['Documents', 'Images', 'Archives', 'Applications', 'Others']
    moved_back_count = 0

    print("Начинаем возврат файлов в исходное состояние...\n")

    for folder_name in created_folders:
        folder_path = target_dir / folder_name
        
        # Если папка существует, возвращаем файлы из неё
        if folder_path.exists() and folder_path.is_dir():
            for item in list(folder_path.iterdir()): # list() нужен, чтобы не изменять структуру во время цикла
                if item.is_file():
                    # Формируем путь возврата в корень папки Downloads
                    original_path = target_dir / item.name
                    
                    # Если файл с таким именем в корне вдруг уже есть, переименовываем
                    counter = 1
                    base_name = item.stem
                    file_extension = item.suffix
                    while original_path.exists():
                        original_path = target_dir / "{}_returned_{}{}".format(base_name, counter, file_extension)
                        counter += 1
                    
                    try:
                        shutil.move(str(item), str(original_path))
                        print("Вернули: {} -> {}".format(item.name, target_dir.name))
                        moved_back_count += 1
                    except Exception as e:
                        print("⚠️ Не удалось вернуть {}. Ошибка: {}".format(item.name, e))
            
            # Если папка опустела, удаляем её
            try:
                if not any(folder_path.iterdir()):
                    folder_path.rmdir()
                    print("Удалена пустая папка: {}".format(folder_name))
            except Exception as e:
                print("Не удалось удалить папку {}: {}".format(folder_name, e))

    print("\nГотово! Вернулось файлов: {}".format(moved_back_count))

if __name__ == "__main__":
    # Укажите тот же путь, где запускали сортировку
    downloads_folder = r"C:\Users\User\Downloads"
    undo_sorting(downloads_folder)