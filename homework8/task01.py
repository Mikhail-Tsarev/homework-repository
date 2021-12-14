class KeyValueStorage:
    """Creates wrapper storage
    for info read from txt file
     Attributes
     ----------
     path: Path for the input file

     Methods
     --------
     __init__: Set all required attributes
     read_file: Open file and get info
    """

    def __init__(self, path: str):
        self.path = path
        self.__filedata = self.read_file()

    def read_file(self):
        with open(self.path, "r") as fi:
            file_data = {}
            for line in fi.readlines():
                key, value = line.strip().split("=")
                if key not in file_data:
                    file_data[key] = int(value) if value.isdigit() else value
        return file_data

    def __getattr__(self, key):
        return self.__filedata[key]

    def __getitem__(self, key):
        return self.__filedata[key]
