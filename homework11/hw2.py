from typing import Callable


class Order:
    """Stores order information

    Attributes
    ----------
    price: Order price
    discount: Type of discount program

    Methods
    --------
    __init__: Set all required attributes
    final_price: Calculates final price"""

    def __init__(self, price: float, discount: Callable = None):
        """
        Set all required attributes

        :param price: Order price
        :param discount: Type of discount program
        """

        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculates final price

        :return: Final price
        """

        if self.discount:
            return self.price - self.discount(self.price)
        return self.price
