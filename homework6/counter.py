def instances_counter(cls: type) -> type:
    """
    Decorator for count created instances
    of the class

    :param cls: Class for decoration
    :return: Decorated class
    """

    cls._created_instances = 0

    def __new__(cls):
        """
        Redefine dunder __new__ method

        :param cls:
        :return: cls instance object
        """

        obj = super(cls, cls).__new__(cls)
        cls._created_instances += 1
        return obj

    @classmethod
    def get_created_instances(cls: type) -> int:
        """
        Counter of created instances of the class

        :param cls: Class
        :return: Number of created instances
        """

        return cls._created_instances

    @classmethod
    def reset_instances_counter(cls: type) -> int:
        """
        Resets the counter of created instances of the class
        and returns number of created class instances
        before reset

        :param cls:
        :return: Number of class instances before reset
        """

        tmp_created_instances = cls._created_instances
        cls._created_instances = 0
        return tmp_created_instances

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls
