#理解思路就是变量(函数def 函数名)定义:可以理解为在内存中生成一个变量，变量中的语句其实并不执行
#			 变量调用(函数名())：函数名() == 内存地址()  调用变量，或者理解为执行变量中的所有语句
#综合来说就是内存有没有

#装饰器decorator(语法糖)：装饰器是一个函数，主要作用是用来包装另一个函数或类，目的是在不改变原函数(类名)的情况下改变被包装对象的行为
#装饰器命名：根据被装饰对象命名（函数装饰器---被装饰对象是函数的  类方法装饰器--被装饰对象是类方法  类装饰器）
#
#特殊装饰器：@property：把ratio方法变成了一个属性，使用的是foo.ratio而不是foo.ratio()。
#装饰器基本构造:高阶函数+函数嵌套+闭包
#高阶函数：一个函数可以作为参数传给另外一个函数（在不改变源代码和调用方式的情况下增加新功能）
#		  或者一个函数的返回值为另外一个函数（覆盖函数名，不修改函数调用）
#函数嵌套：一个函数def内定义了函数def（局部作用域），return 函数名，即返回函数的内存地址
#闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。
#
#函数装饰器：指装饰器是一个函数，传入的是一个函数，返回的是另一个函数
#
#@use_logging   # foo = use_logging(foo)    foo是传入foo函数的内存地址，foo()是执行函数
#foo()          # 函数名() == 内存地址()    内存地址可以由高阶函数和嵌套函数return得到



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

import time        #第一步
user, passwd = "111", "123"  #第二步

def auth(auth_type):            #第三步(定义) #第六步(调用) #使用了闭包，所以被装饰函数才可以使用参数auth_type
    print("auth_type:", auth_type)   #第七步
    # 装饰器有参数添加一层
    def outer_wrapper(func):      #第八步(定义) #第十步(调用)  #使用函数嵌套 和 高级函数
        def wrapper(*args, **kwargs):   #第十一步
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()            
                if user == username and passwd == password:
                    print("\033[32:1mUser has passwd auth successd\033[0m")
                    res = func(*args, **kwargs)
                    print("----after----")
                    return res
                else:
                    exit("\033[31;1minvalid username or passwd\033[0m")
            elif auth_type == "ldap":
                print("ldap认证")

        return wrapper          #第十二步 #使用高级函数

    return outer_wrapper    #第九步


def index():      #第四步
    print("welcome to index page")


# @auth()相当于执行了函数，本来是返回outer_wrapper,但是一执行就返回wrapper，因此auth_type判断是在wrapper内部
# @auth()相当于执行了函数, 返回outer_wrapper，然后@auth语法糖又要执行一遍函数，相当于执行outer_wrapper(func)
@auth(auth_type="local")     #第五步
def home():
    print("welcome to home page")
    # 被装饰函数如果有return返回值，则在装饰函数上也需要return返回
    return "from home"


@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")


index()
print(home())    #这里的home经过语法糖@auth(auth_type="local") 和 @auth 两次调用，实际home变量指向wrapper函数体地址
bbs()
