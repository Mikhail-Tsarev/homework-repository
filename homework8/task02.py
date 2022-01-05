import sqlite3
from typing import Any


class TableData(dict):
    """Wrapper class for database table

    Attributes
    ----------
    db_name: path (name) of the database
    table_name: Name of the table

    Methods
    --------
    __init__: Set all required attributes
    __len__: Returns length of the table
    __getitem__: Returns single record by key
    __contains__: Checks if value exists in column
    __iter__: Returns iterator object for request result
    """

    def __init__(self, db_name, table_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.table = table_name
        self.cursor = self.conn.cursor()

    def __len__(self) -> int:
        """Getting the length of the table"""

        data = self.cursor.execute(f"SELECT * from {self.table}").fetchall()
        return len(data)

    def __getitem__(self, key: str) -> Any:
        """Getting the single record by key"""

        query = f"SELECT * from {self.table} where name='{key}'"
        data = self.cursor.execute(query).fetchone()
        return data

    def __contains__(self, key: str) -> bool:
        """Checks if value exists in column

        :param key: Search key
        :return: Is value in column
        """

        query = f"SELECT * from {self.table} where name='{key}'"
        data = self.cursor.execute(query).fetchone()
        return bool(data)

    def __iter__(self):
        """Returns iterator object for request result (cursor itself)"""

        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        return cursor
