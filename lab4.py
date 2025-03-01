if __name__ == "__main__":
    # Write your solution here
    class TransportVehicle:
        """
        Базовый класс для всех транспортных средств.
        Атрибуты:
            - brand: марка транспортного средства.
            - model: модель транспортного средства.
            - year: год выпуска.
            - fuel_type: тип топлива.
        """

        def __init__(self, brand: str, model: str, year: int, fuel_type: str):
            """
            Конструктор базового класса.
            :param brand: Марка транспортного средства.
            :param model: Модель транспортного средства.
            :param year: Год выпуска.
            :param fuel_type: Тип топлива.
            """
            self.brand = brand
            self.model = model
            self.year = year
            self.fuel_type = fuel_type

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.
            :return: Строка с описанием транспортного средства.
            """
            return f"{self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.
            :return: Формальная строка для отладки.
            """
            return f"TransportVehicle(brand={self.brand}, model={self.model}, year={self.year}, fuel_type={self.fuel_type})"

        def start_engine(self) -> str:
            """
            Запуск двигателя транспортного средства.
            :return: Сообщение о запуске двигателя.
            """
            return f"Двигатель {self.brand} {self.model} запущен."


    class PassengerCar(TransportVehicle):
        """
        Дочерний класс для легковых автомобилей.
        Дополнительные атрибуты:
            - num_doors: количество дверей.
            - max_speed: максимальная скорость.
        """

        def __init__(self, brand: str, model: str, year: int, fuel_type: str, num_doors: int, max_speed: int):
            """
            Конструктор дочернего класса.
            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска.
            :param fuel_type: Тип топлива.
            :param num_doors: Количество дверей.
            :param max_speed: Максимальная скорость.
            """
            super().__init__(brand, model, year, fuel_type)
            self.num_doors = num_doors
            self.max_speed = max_speed

        def __str__(self) -> str:
            """
            Перегрузка метода __str__ для легкового автомобиля.
            :return: Строка с описанием легкового автомобиля.
            """
            return f"{self.brand} {self.model} ({self.year}), {self.num_doors} дверей, макс. скорость: {self.max_speed} км/ч"

        def __repr__(self) -> str:
            """
            Перегрузка метода __repr__ для легкового автомобиля.
            :return: Формальная строка для отладки.
            """
            return (f"PassengerCar(brand={self.brand}, model={self.model}, year={self.year}, "
                    f"fuel_type={self.fuel_type}, num_doors={self.num_doors}, max_speed={self.max_speed})")

        def start_engine(self) -> str:
            """
            Перегрузка метода start_engine для легкового автомобиля.
            :return: Сообщение о запуске двигателя с учётом типа автомобиля.
            """
            return f"Двигатель легкового автомобиля {self.brand} {self.model} запущен."


    class Truck(TransportVehicle):
        """
        Дочерний класс для грузовых автомобилей.
        Дополнительные атрибуты:
            - cargo_capacity: грузоподъёмность (в тоннах).
            - num_axles: количество осей.
        """

        def __init__(self, brand: str, model: str, year: int, fuel_type: str, cargo_capacity: float, num_axles: int):
            """
            Конструктор дочернего класса.
            :param brand: Марка грузовика.
            :param model: Модель грузовика.
            :param year: Год выпуска.
            :param fuel_type: Тип топлива.
            :param cargo_capacity: Грузоподъёмность (в тоннах).
            :param num_axles: Количество осей.
            """
            super().__init__(brand, model, year, fuel_type)
            self.cargo_capacity = cargo_capacity
            self.num_axles = num_axles

        def __str__(self) -> str:
            """
            Перегрузка метода __str__ для грузового автомобиля.
            :return: Строка с описанием грузового автомобиля.
            """
            return f"{self.brand} {self.model} ({self.year}), грузоподъёмность: {self.cargo_capacity} т, оси: {self.num_axles}"

        def __repr__(self) -> str:
            """
            Перегрузка метода __repr__ для грузового автомобиля.
            :return: Формальная строка для отладки.
            """
            return (f"Truck(brand={self.brand}, model={self.model}, year={self.year}, "
                    f"fuel_type={self.fuel_type}, cargo_capacity={self.cargo_capacity}, num_axles={self.num_axles})")

        def load_cargo(self, weight: float) -> str:
            """
            Метод для загрузки груза.
            :param weight: Вес груза (в тоннах).
            :return: Сообщение о загрузке.
            """
            if weight <= self.cargo_capacity:
                return f"Груз весом {weight} т успешно загружен."
            else:
                return f"Груз весом {weight} т превышает грузоподъёмность."


    # Пример использования
    car = PassengerCar("Toyota", "Corolla", 2020, "бензин", 4, 180)
    truck = Truck("Volvo", "FH16", 2019, "дизель", 20.0, 3)

    print(car)  # Toyota Corolla (2020), 4 дверей, макс. скорость: 180 км/ч
    print(truck)  # Volvo FH16 (2019), грузоподъёмность: 20.0 т, оси: 3

    print(car.start_engine())  # Двигатель легкового автомобиля Toyota Corolla запущен.
    print(truck.load_cargo(15))  # Груз весом 15 т успешно загружен.
    pass
