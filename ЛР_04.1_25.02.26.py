class Vehicle:
    """
    Базовый класс транспортного средства.

    Содержит общие атрибуты и методы для всех видов транспорта.
    Атрибуты make, model, year сделаны защищёнными, чтобы предотвратить
    их прямое изменение извне (инкапсуляция). Для доступа к ним используются
    публичные свойства.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализирует транспортное средство.

        :param make: Марка
        :param model: Модель
        :param year: Год выпуска
        """
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self) -> str:
        """Возвращает марку (только для чтения)."""
        return self._make

    @property
    def model(self) -> str:
        """Возвращает модель (только для чтения)."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска (только для чтения)."""
        return self._year

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Строка с информацией о запуске двигателя.
        """
        return f"Двигатель {self._make} {self._model} запущен."

    def get_description(self) -> str:
        """
        Возвращает базовое описание транспортного средства.

        :return: Строка с маркой, моделью и годом.
        """
        return f"{self._make} {self._model}, {self._year} г."

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return self.get_description()

    def __repr__(self) -> str:
        """Официальное строковое представление для отладки."""
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, year={self._year!r})"


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующий от Vehicle.

    Добавляет атрибут capacity (грузоподъёмность в тоннах),
    который также защищён и доступен через свойство с проверкой.
    Перегружает метод get_description, чтобы включить информацию о грузоподъёмности.
    Метод start_engine унаследован без изменений.
    """

    def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализирует грузовой автомобиль.

        :param make: Марка
        :param model: Модель
        :param year: Год выпуска
        :param capacity: Грузоподъёмность в тоннах (должна быть положительной)
        """
        super().__init__(make, model, year)
        self.capacity = capacity  # используем сеттер для проверки

    @property
    def capacity(self) -> float:
        """Возвращает грузоподъёмность."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: float) -> None:
        """
        Устанавливает грузоподъёмность с проверкой.

        :param value: Новое значение грузоподъёмности (должно быть положительным числом)
        :raises ValueError: Если значение <= 0
        """
        if value <= 0:
            raise ValueError("Грузоподъёмность должна быть положительной")
        self._capacity = float(value)

    def get_description(self) -> str:
        """
        Возвращает описание грузового автомобиля, включая грузоподъёмность.

        Перегрузка метода необходима, потому что для грузового автомобиля
        важно указывать его грузоподъёмность при описании.
        """
        base_desc = super().get_description()
        return f"{base_desc} Грузоподъёмность: {self._capacity} т."

    def __repr__(self) -> str:
        """Перегружен для включения capacity в строку."""
        return (f"{self.__class__.__name__}(make={self._make!r}, "
                f"model={self._model!r}, year={self._year!r}, capacity={self._capacity!r})")


if __name__ == "__main__":
    # Пример использования
    truck = Truck("Volvo", "FH16", 2020, 18.5)
    print(truck.start_engine())  # унаследованный метод
    print(truck.get_description())  # перегруженный метод
    print(truck)  # __str__
    print(repr(truck))  # __repr__