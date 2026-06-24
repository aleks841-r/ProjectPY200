# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

from bucket import Bucket
from disk import Disk

if __name__ == "__main__":
    # Инициализируем маленькую флешку на 0.01 МБ для быстрой демонстрации лимита
    flash_drive = Disk(total_space_mb=0.01)

    count = 0
    try:
        # Пытаемся безостановочно записывать пустые файлы нулевого размера
        while True:
            empty_file = Bucket(max_volume=1.0)
            flash_drive.save_bucket(empty_file)
            count += 1
    except ValueError as e:
        print(f"Запись остановлена!")
        print(f"Удалось записать пустых файлов: {count} шт.")
        print(f"Финальное занятое место (метаданные): {flash_drive.get_used_space_mb():.4f} МБ")
```
