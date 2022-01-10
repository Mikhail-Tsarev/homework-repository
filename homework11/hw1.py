class SimplifiedEnum(type):
    """Metaclass for enum sizes and colors"""

    def __new__(mcs, name, bases, classdict):
        cls_instance = super().__new__(mcs, name, bases, classdict)
        for attr in classdict[f"_{name}__keys"]:
            setattr(cls_instance, attr, attr)
        return cls_instance


class ColorsEnum(metaclass=SimplifiedEnum):
    """Class for colors
    Use __keys list for enumeration"""

    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    """Class for sizes
    Use __keys list for enumeration"""

    __keys = ("XL", "L", "M", "S", "XS")
