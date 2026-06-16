import shutil
from pathlib import Path

def sort_files(target_directory):
    FILE_CATEGORIES = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Applications': ['.exe', '.msi', '.dmg']
    }

    target_dir = Path(target_directory)

    # Проверяем директорию
    if not target_dir.exists() or not target_dir.is_dir():
        print("Ошибка: Путь '{}' не существует или не является папкой.".format(target_directory))
        return

    print("Начинаем сортировку в: {}\n".format(target_dir.resolve()))
    moved_count = 0

    # Перебираем файлы
    for item in target_dir.iterdir():
        if item.is_dir() or item.name.startswith('.'):
            continue

        file_extension = item.suffix.lower()
        
        if not file_extension:
            destination_folder = 'Others'
        else:
            destination_folder = 'Others'
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder = category
                    break

        create_dir_path = target_dir / destination_folder
        create_dir_path.mkdir(exist_ok=True)

        new_item_path = create_dir_path / item.name
        
        # Обработка дубликатов
        counter = 1
        base_name = item.stem
        is_renamed = False
        
        while new_item_path.exists():
            new_item_path = create_dir_path / "{}_{}{}".format(base_name, counter, file_extension)
            counter += 1
            is_renamed = True
            
        # Перемещение 
        try:
            shutil.move(str(item), str(new_item_path))
            log_message = "Перемещен: {} -> {}/".format(item.name, destination_folder)
            if is_renamed:
                log_message += " (переименован в {})".format(new_item_path.name)
            print(log_message)
            
            moved_count += 1
        except Exception as e:
            print("⚠️ Не удалось переместить {}. Ошибка: {}".format(item.name, e))

    print("\nСортировка завершена! Перемещено файлов: {}".format(moved_count))

if __name__ == "__main__":
    folder_to_sort = r"C:\Users\User\Downloads" 
    sort_files(folder_to_sort)