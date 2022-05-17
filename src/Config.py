from csv import DictReader

class Config:

    def __init__(self):
        self.data: list = None

    def open(self, path: str) -> bool:
        try:
            with open(path) as file:
                reader = DictReader(file)
                self.data = list(reader)
            return True
        except FileNotFoundError:
            raise FileNotFoundError("File not found at '" + path + "'.")

    def get(self, service: str, value: str) -> str | bool | int | float:
        try:
            for i in self.data:
                if i["service"] == service:
                    return i[value]
        except TypeError:
            return None