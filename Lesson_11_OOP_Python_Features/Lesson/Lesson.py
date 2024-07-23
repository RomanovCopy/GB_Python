# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#         # принтим только в учебных целях, а не для реальных задач
#         print(
#             f"Создал {self} со свойствами: \n"
#             f"{self.name = },\t{self.equipment=},\t{self.life=}"
#         )


# print("Создаем первый раз")
# u_1 = User("Спенглер")
# print("Создаем второй раз")
# u_2 = User("Венкман", ["протонный ускоритель", "ловушка"])
# print("Создаем третий раз")
# u_3 = User(equipment=["ловушка", "прибор ночного видения"], name="Стэнц")


# class User:
#     def __init__(self, name: str):
#         self.name = name
#         # принтим только в учебных целях, а не для реальных задач
#         print( f"Создал {self} со свойствами: \n"
#             f"{self.name = }" )

#     def __new__(cls, *args, **kwargs):
#         instance=super().__new__(cls)
#         print(f'Создал класс {cls}')
#         return instance


# print("Создаем первый раз")
# u_1 = User("Спенглер")
# print("Создаем второй раз")
# u_2 = User("Венкман")
# print("Создаем третий раз")
# u_3 = User( name="Стэнц")


# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f"Создал класс {cls}")
#         return instance


# print("Создаем первый раз")
# a = NamedInt(42, "Главный ответ жизни, Вселенной и вообще")
# print("Создаем второй раз")
# b = NamedInt(73, "Лучше просто число")
# print(f"{a=}\t{a.name=}\t{type(a)=}")
# print(f"{b=}\t{b.name=}\t{type(b)=}")
# c = a + b
# print(f"{c=}\t{type(c)=}")


# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self, name: str):
#         self.name = name

# a=Singleton('Первый')
# print(f'{a.name=}')
# b=Singleton('Второй')
# print(f'{a is b =}')
# print(f'{a.name=}\t{b.name=}')


import sys

class User:
    def __init__(self, name: str):
        self.name = name
        print( f"Создал {self.name = }" )

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')

u_1 = User("Спенглер")
print(sys.getrefcount(u_1))
u_2=u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
print('Завершение работы')

