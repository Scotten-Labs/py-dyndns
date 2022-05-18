from csv import DictReader

class Config:

    def __init__(self):
        self.data: list = None

    def open(self, path: str) -> bool:
        """Opens config file. Formatted as a CSV.

        Args:
            path (str): Path to File

        Raises:
            FileNotFoundError: File not Found

        Returns:
            bool: True when Opened
        """
        try:
            with open(path) as file:
                reader = DictReader(file)
                self.data = list(reader)
            return True
        except FileNotFoundError:
            raise FileNotFoundError("File not found at '" + path + "'.")

    def get(self, service: str, value: str) -> str | bool | int | float:
        """Returns the key pair from the config file.

        Args:
            service (str): Service Name
            value (str): Key Value

        Returns:
            str | bool | int | float: Key Value
        """
        try:
            for i in self.data:
                if i["service"] == service:
                    return i[value]
        except TypeError:
            return None