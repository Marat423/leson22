class House: # Создаем Класс

    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return instance


    def __init__(self, name, number_is_floors): # Метод и атрибуты
        self.name = name
        self.number_is_floors = number_is_floors

   # def __len__(self):
     #   return self.number_is_floors

    def __str__(self):
        return str(f'Название Жк: {self.name}, кол-во этажей {self.number_is_floors}')
        return name_nambers


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_is_floors == other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors == other


    def __add__(self, value):
        if isinstance(value, int):
            self.number_is_floors += value
            return self

    def __iadd__(self, value):
        self.number_is_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)



    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_is_floors < other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_is_floors <= other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_is_floors > other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_is_floors >= other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_is_floors != other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors != other




    def __del__(self):
        print(f' {self.name} снесёен, но он остается в истории.')





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)

