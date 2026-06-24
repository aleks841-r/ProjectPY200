import math
from types import SimpleNamespace
from n_file import File


class Conv:
    COEFFICIENTS = {
        "nHD": 1,
        "HD": 4,
        "FullHD": 9,
        "2K": 16,
        "4K": 36
    }

    def conv_to(self, file: File, size: int):
        """Выполняет конвертирование формата"""
        target_key = next(k for k, v in File.RESOLUTIONS.items() if v == file.resolution)
        target_value = self.COEFFICIENTS[target_key]
        filtered_ = [
            (k, v) for k, v in self.COEFFICIENTS.items()
            if v <= target_value
        ]
        reversed_ = filtered_[::-1]
        for key, value in reversed_:
            s = int(math.ceil(file.size * value/ target_value))
            if s > size:
                continue
            else:
                print(f"Исходный файл:\n{file}")
                file.size = s
                file.resolution = File.RESOLUTIONS[key]
                print(f"Новый файл:\n{file}")
                break
        else:
            raise ValueError(
                f"[!!!] Ошибка: Невозможно добавить {file.name} объемом {file.size}."
                f"\n[!!!] На flash накопителе доступно: {size}"
                )


if __name__ == "__main__":
    file = Conv()
    file.data = SimpleNamespace(
            name="file8", resolution=(2560, 1440), size=4000
        )
    result = file.conv_to(file.data, 400)