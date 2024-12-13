# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
class Fruit:
    def __init__(self, name: str, weight: float, colour: str):
        """
        Инициализация объекта Фрукт.

        :param name: Название фрукта
        :param weight: Вес фрукта в граммах
        :param colour: Цвет фрукта

        Примеры:
        >>> fruit = Fruit(apple, 76.8, green)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int/float")
        if weight <= 0:
            raise ValueError("Вес фрукта должен быть положительным числом.")
        self.weight = weight

        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = colour

    def cut(self, piece:int) -> float:
        """
        Порезать фрукт на равные куски и вывести массу каждого из них.
        :param piece: Количество кусков
        :return: Масса куска
        Примеры:
        >>> fruit = Fruit(orange, 102.3, orange)
        >>> fruit.cut(6)
        """
        if not isinstance(piece, int):
            raise TypeError("Количество кусков должно быть целым числом")
        if piece < 2:
            raise ValueError("Количество кусков должно быть не меньше двух")

    def juice(self) -> float:
        """
        Объём сока, получаемого из фрукта.
        :return: Объём сока
        Примеры:
        >>> fruit = Fruit(banana, 86.4, yellow)
        >>> fruit.juice()
        """

class Vehicle:
    def __init__(self, model: str, year: int, max_speed: float, price: float):
        """
        Инициализация объекта Транспорт.

        :param model: Модель транспортного средства
        :param year: Год выпуска
        :param max_speed: Максимальная скорость в км/ч
        :param price: Цена машины в рублях

        Примеры:
        >>> vehicle = Vehicle(Honda, 2005, 177, 1600000)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if max_speed <= 1980:
            raise ValueError("Слишком старая модель.")
        self.year = year

        if not isinstance(max_speed, float):
            raise TypeError("Максимальная скорость должна быть типа float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        self.max_speed = max_speed

        if not isinstance(price, float):
            raise TypeError("Цена должна быть типа float")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом.")
        self.price = price

    def acceleration(self, accspeed: float) -> float:
        """
        Рассчитать время ускорения до определенной скорости.
        :param accspeed: Конечная скорость
        :raise ValueError: Если заданная скорость выше максимальной
        :return: Время ускорения
        Примеры:
        >>> vehicle = Vehicle(Toyota, 2012, 220, 3600000)
        >>> vehicle.acceleration(100)
        """
        if not isinstance(accspeed, (int, float)):
            raise TypeError("Конечная скорость должна быть типа int/float")
        if accspeed < 0:
            raise ValueError("Конечная скорость должна быть положительным числом")

    def braking(self, breakspeed: float) -> float:
        """
        Рассчитать тормозной путь от текущей скорости.
        :param breakspeed: Текущая скорость
        :raise ValueError: Если заданная скорость выше максимальной
        :return: Длина тормозного пути
        Примеры:
        >>> vehicle = Vehicle(Ford, 1991, 180, 2800000)
        >>> vehicle.braking(165)
        """
        if not isinstance(breakspeed, (int, float)):
            raise TypeError("Текущая скорость должна быть типа int/float")
        if breakspeed < 0:
            raise ValueError("Текущая скорость должна быть положительным числом")


class ShareStock:
    def __init__(self, entity: str, current_price: dict, shares_owned: dict):
        """
        Инициализация объекта Акции.

        :param entity: Держатель акций
        :param current_price: Текущая цена акций различных компаний в долларах
        :param shares_owned: Количество имеющихся акций той или иной компании

        Примеры:
        >>> vehicle = Vehicle(AllIvnest, curprice, AIown)
        """

        if not isinstance(entity, str):
            raise TypeError("Наименование держателя должно быть типа str")
        self.entity = entity

        if not isinstance(current_price, dict):
            raise TypeError("Перечень должен быть типа dict")
        self.current_price = current_price

        if not isinstance(shares_owned, dict):
            raise TypeError("Перечень должен быть типа dict")
        self.shares_owned = shares_owned

    def purchase(self, seller: str, purchase_num: int) -> None:
        """
        Метод для покупки акций
        :param seller: Компания, чьи акции приобретаются
        :param purchase_num: Количество покупаемых акций
        :return: shares_owned
        Примеры:
        >>> stockshare = ShareStock(WhiteLake, curprice, WLown)
        >>> stockshare.purchase(GazProm, 1)
        """
        if not isinstance(seller, str):
            raise TypeError("Наименование должно быть типа str")
        if not isinstance(purchase_num, int):
            raise TypeError("Количество акций должно быть типа int")
        if purchase_num < 1:
            raise ValueError("Количество акций должно быть не меньше одной")


    def sell(self, sell_ent: str, sell_num: int) -> None:
        """
        Метод для продажи акций
        :sell_ent: Компания, чьи акции продаются
        :param sell_num: Количество продаваемых акций
        :return: shares_owned
        Примеры:
        >>> stockshare = ShareStock(DBank, curprice, DBown)
        >>> stockshare.sell(Apple, 127)
        """
        if not isinstance(sell_ent, str):
            raise TypeError("Наименование должно быть типа str")
        if not isinstance(sell_num, int):
            raise TypeError("Количество акций должно быть типа int")
        if sell_num < 1:
            raise ValueError("Количество акций должно быть не меньше одной")


    def get_value(self) -> float:
        """
        Метод для получения общей стоимости акций.
        :return: Стоимость всех акций держателя
        Примеры:
        >>> stockshare = ShareStock(RelaTable, curprice, RTown)
        >>> stockshare.get_value()
        """




if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
