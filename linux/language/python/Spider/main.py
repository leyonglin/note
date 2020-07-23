
import requests

######################## get ################################

url="http://www.baidu.com"

response=requests.get(url)

# response.encoding = 'utf8'

# text是程序自己猜测给出的编码，content可以自己指定编码
# print(response.text)
print(response.content.decode('utf8'))

# https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html#id2
# print(dir(response))
# print(dir(response.status_code))
# print(dir(response.request))
# print(response.request.headers)


######################## header #################################


url="http://www.baidu.com"


# 可以在headers中添加cookie,refer等
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response=requests.get(url)
print(len(response.content.decode()))

response1=requests.get(url, headers=headers)
print(len(response1.content.decode()))


####################### param ################################

url="http://www.baidu.com/s?"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

data = {
    'wd': 'python'
}

# timeout超时为3秒 ， verify不进行ca证书认证(有些网站证书过期但是点高级还是能使用)
response=requests.get(url, headers=headers, params=data, timeout=3, verify=False)

print(response.url)



####################### cookiejar ##################################

url="http://www.baidu.com"


# 可以在headers中添加cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response = requests.get(url)

#cookiejar
print(response.cookies)
# print(dir(requests.utils))
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)


######################### proxies ###############################


url="http://www.baidu.com"


# 可以在headers中添加cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

proxies = {
    'http': 'http://47.108.31.89:8118',
}

response=requests.get(url,headers=headers,proxies=proxies)
with open('www.baidu.com.html', 'wb')as f:
    f.write(response.content)



