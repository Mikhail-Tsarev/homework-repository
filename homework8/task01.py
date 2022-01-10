class KeyValueStorage:
    """Creates wrapper storage
    for info read from txt file

    Attributes
    ----------
    path: Path to the input file

    Methods
    --------
    __init__: Set all required attributes
    read_file: Open file and get info
    """

    def __init__(self, path: str):
        """Sets all required attrs

        path: Path to the input file
        """

        self.path = path
        self.__filedata = self.read_file()

    def read_file(self) -> dict:
        """
        Read input file and stores data into dict

        :return: Dict with data from file
        """

        with open(self.path, "r") as fi:
            file_data = {}
            for line in fi.readlines():
                key, value = line.strip().split("=")
                if key not in file_data:
                    file_data[key] = int(value) if value.isdigit() else value
        return file_data

    def __getattr__(self, key):
        """
        Getting attr by key

        :param key: Key of the dict
        :return: Value
        """

        return self.__filedata[key]

    def __getitem__(self, key):
        """Getting the single record by key

        :param key: Key to search by
        :return: Value
        """

        return self.__filedata[key]
