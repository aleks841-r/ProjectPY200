class File:
    RESOLUTIONS = {
        "nHD": (640, 360),
        "HD": (1280, 720),
        "FullHD": (1920, 1080),
        "2K": (2560, 1440),
        "4K": (3840, 2160)
    }

    def __init__(self, name: str, resolution: tuple[int, int], size: int):
        """Выполняет проверку имени, разрешения и размера файла

        :param name: имя файла
        :param resolution: разрешение
        :param size: размер файла
        """
        if not (name.isalnum() and name.isascii()):
            raise ValueError(f"[!!!] ОШИБКА. В имени файла должны быть только латинские буквы и/или цифры!")

        if not isinstance(size, int):
            raise TypeError(f"[!!!] ОШИБКА. Размер файла должен быть целым числом!")

        if size < 0:
            raise ValueError(f"[!!!] ОШИБКА. Размер файла должен быть больше 0")

        if resolution is not None:
            if resolution not in self.RESOLUTIONS.values():
                raise ValueError(f"[!!!] ОШИБКА. Разрешение {resolution} не поддерживается!")

        self.name = name
        self.size = size
        self.resolution = resolution

    def to_dict(self):
        #return {"file_name": self.name, "resolution": self.resolution, "size": self.size}
        return {"resolution": self.resolution, "size": self.size}

    def __str__(self) -> str:
        """Выводит объект класса (экземпляр класса File) на печать"""
        w, h = self.resolution
        return f"имя файла: {self.name}, разрешение: {w}x{h}, размер {self.size}"

if __name__ == "__main__":
    try:
        file1 = File(name="file5", resolution=(1280,720), size=100)
        print(file1)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)