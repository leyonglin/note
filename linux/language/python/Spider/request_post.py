# coding:utf-8
import requests
import js2py
import json

def login():
    #创建session对象
    session = requests.session()
    #设置请求头
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    #发送获取公钥数据包的get请求,因为有部分数据从这里来或者以来这里的数据
    response = session.get('http://www.renren.com/ajaxLogin')
    data_get = response.content.decode()
    print(data_get)
    #获取前置条件(js变量和js代码)
    n = json.loads(data_get)['data']
    t = {
        "password": "password"
    }
    rsa_js = session.get('http://www.renren.com/ajaxLogin.js').content.decode()
    #创建js环境对象
    context = js2py.EvalJs()
    #执行前置变量和js代码加载到环境对象中(为关键代码做好必要准备)
    context.execute(rsa_js)
    context.n = n
    context.t = t
    #执行关键js
    pwd_js = """
        t.password = t.password
        setMaxDigits()
        var o = ...
           ,r = ...
    """
    context.execute(pwd_js)
    #获取加密密码
    print(context.r)
    #构建formdata
    formdata = {
        "phone": "1111111",
        "password": context.r,
        "c1": -100,
        "rKey": n['rKey']
    }
    print(formdata)
    #发送post请求，模拟登陆
    response = session.post('http://www.renren.com/ajaxLogin',data=formdata)
    #验证
    print(response.content.decode())

if __name__ == '__main__':
    login()


