# 无参数装饰器
# import time
#
#
# # 1.修改函数情况下运行
# # def deco(func):
# #     start_time = time.time()
# #     func()
# #     stop_time = time.time()
# #     print('the func run time is %s' % (start_time - stop_time))
#
# # 2.不修改调用方式
# func就是传入参数
# def timer(func):
#     # 声明函数变量
#     def deco():
#         # print(deco)
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('the func run time is %s' % (start_time - stop_time))
#
#     # 返回函数变量的内存地址，这样接收者便能根据内存地址调用
#     return deco
#
#
# # @timer 相当于 test1 = timer(test1)
# @timer
# def test1():
#     time.sleep(2)
#     print('in the test1')
#
#
# # @timer 相当于 test2 = timer(test2)
# @timer
# def test2():
#     time.sleep(2)
#     print('in the test2')
#
#
# # 1.修改函数情况下运行
# # deco(test1)
# # deco(test2)
#
# # 2.不修改调用方式
# # 接收函数返回值，及内存地址并进行调用
# # test1 = timer(test1)
# # # print(test1)
# # test1()
# #
# # test2 = timer(test2)
# # test2()
#
# # 在被装饰函数前面加上@装饰器名
# test1()
# test2()

####################################################################################

# # 被装饰函数带参数
# import time
#
#
# def timer(func):
#     def deco(*args, **kwargs):
#         start_time = time.time()
#         func(*args,**kwargs)
#         stop_time = time.time()
#         print('the func run time is %s' % (start_time - stop_time))
#
#     return deco
#
#
# @timer
# def test1():
#     time.sleep(2)
#     print('in the test1')
#
# # test2 = timer(test2)  而timer返回值是deco的内存地址, 即test2() = deco()，因此test2(name) = deco(name)
# @timer
# def test2(name):
#     time.sleep(2)
#     print('test2 have arg', name)
#
#
# test1()
# test2("lin")


####################################################################################

# 装饰器和被装饰函数带参数，这一部分用断点调试

user, passwd = "111", "123"


def auth(auth_type):
    print("auth_type:", auth_type)

    # 装饰器有参数添加一层
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            username = input("username:").strip()
            password = input("password:").strip()
            if auth_type == "local":
                if user == username and passwd == password:
                    print("\033[32:1mUser has passwd auth successd\033[0m")
                    res = func(*args, **kwargs)
                    print("----after----")
                    return res
                else:
                    exit("\033[31;1minvalid username or passwd\033[0m")
            elif auth_type == "ldap":
                print("ldap认证")

        return wrapper

    return outer_wrapper


def index():
    print("welcome to index page")


# auth()相当于执行了函数，本来是返回outer_wrapper,但是一执行就返回wrapper，因此auth_type判断是在wrapper内部
@auth(auth_type="local")
def home():
    print("welcome to home page")
    # 被装饰函数如果有return返回值，则在装饰函数上也需要return返回
    return "from home"


@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")


index()
print(home())
bbs()
