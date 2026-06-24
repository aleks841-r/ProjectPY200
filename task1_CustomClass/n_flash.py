import doctest
import json
import os
from pathlib import Path
from n_file import File
from n_converter import Conv


class Flash:
    def __init__(self, file_name="flash.json", max_size=1000):
        """Задаёт значения по умолчанию и запускает метод _init_flash

        :param file_name: название накопителя
        :param max_size: объём накопителя

        >>> flash = Flash("my_flash.json", 1000)
        >>> flash._init_flash()
        'my_flash.json'
        """
        self.flash = file_name
        self.flash_name = Path(file_name).stem
        self.max_size = max_size
        self.conv_size = Conv()
        self._init_flash()

    def _init_flash(self):
        """Инициирует создание flash накопителя (flash.json, если его не было)"""
        if not os.path.exists(self.flash) or os.path.getsize(self.flash) == 0:
            with open(self.flash, "w", encoding="utf-8") as f:
                json.dump({}, f)
                print(f"Создан новый flash накопитель {self.flash_name} ёмкостью {self.max_size}")
        elif self.total > self.max_size:
            with open(self.flash, "w", encoding="utf-8") as f:
                json.dump({}, f)
                print(f"Flash накопитель {self.flash_name} ёмкостью {self.max_size} отформатирован")
        return self.flash

    def read(self):
        """Возвращает содержимое flash накопителя (flash.json)"""
        with open(self.flash, "r", encoding="utf-8") as f:
            return json.load(f)

    @property
    def total(self):
        """Возвращает суммарный объём всех файлов на flash накопителе"""
        data = self.read()
        return sum(file_size["size"] for file_size in data.values())

    def add_file(self, file: File):
        """Добавляет новый файл на flash накопитель"""
        current_data = self.read()

        # Проверяет выполнение условий: имя файла и суммарный объём
        if file.name in current_data:
            raise ValueError(
                f"[!!!] Ошибка: Невозможно добавить {file.name}"
                f"\n[!!!] Файл с таким именем уже существует на flash накопителе!"
            )
        if self.total + file.size > self.max_size:
            size = self.max_size - self.total
            self.conv_size.conv_to(file, size)

        current_data[file.name] = file.to_dict()

        with open(self.flash, "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)

        print(f"Файл '{file.name}' успешно записан на flash накопитель.")

    def del_file(self, file: File):
        """Удаляет файл с flash накопителя"""
        current_data = self.read()

        # Проверяет наличие файла на flash накопителе
        if file.name not in current_data:
            files = []
            for name, info in current_data.items():
                files.append(f"{name}, разрешение: {info['resolution']}, объём: {info['size']}")
            format_ ="\n".join(files)
            print(f"\n{' ' * 17}Файлы на {self.flash_name}:\n{'*' * 50}\n{format_}\n{'*' * 50}\n")
            raise ValueError(f"[!!!] Ошибка. Файл {file.name} отсутствует на flash накопителе!")

        current_data.pop(file.name)
        with open(self.flash, "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)

        print(f"Файл {file.name} успешно удален c flash накопителя.")

    def __str__(self):
        """Выводит объект класса (экземпляр класса Flash) на печать"""
        current_data = self.read()

        if not current_data:
            return "На flash накопителе нет файлов"

        files = []
        for name, info in current_data.items():
            files.append(f"{name}, разрешение: {info['resolution']}, объём: {info['size']}")

        return "\n".join(files)


def main():
    """Запуск тестов и обработка ошибок"""
    try:
        doctest.testmod(verbose=True)

        my_flash = Flash("flash.json", 1000)

        file1 = File(name="file3", resolution=(1280,720), size=1400)
        #file1 = File(name="file77", resolution=(2560,1440), size=4000)
        #file1 = File(name="file4", resolution=(3840,2160), size=4800)

        my_flash.add_file(file1)
        #my_flash.del_file(file1)

    except ValueError as e:
        print(e)

    #print(f"\n{' ' * 12}Файлы на flash накопителе:\n{'*' * 50}\n{my_flash}\n")

if __name__ == "__main__":
    main()