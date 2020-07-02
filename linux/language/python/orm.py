# from datetime import datetime, date
#
#
# class User():
#     def __init__(self, name, birthday):
#         self.name = name
#         self.birthday = birthday
#         # 一个_表示不希望被直接调用，但是可以被直接调用，__表示不被直接调用，原理是重命名该属性
#         # self._age = 0
#
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#     @age.setter
#     def age(self, value):
#         self._age = value
#
#
# if __name__ == '__main__':
#     user = User("bobby", date(year=1993, month=1, day=1))
#     # @property就是将方法变成属性方式调用
#     print(user.age)
#     # @age.setter赋值
#     user.age = 30
#     print(user._age)


# 属性描述符
# import numbers
#
#
# class IntFiled:
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         if not isinstance(value, numbers.Integral):
#             raise ValueError("int value need")
#         self.value = value
#
#     def __delete__(self, instance):
#         pass
#
#
# class User:
#     age = IntFiled()
#
#
# if __name__ == '__main__':
#     user = User()
#     print(type(user))
#     user.age = 30
#     print(user.age)

# class MyMetaClass(type):
#     def __new__(cls, name, bases, attrs, **kwargs):
#         pass
