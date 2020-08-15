
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


######################## header and cookie #################################


url="http://www.baidu.com"


# 可以在headers中添加cookie,refer等
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

#Cookie_temp = '_ga=GA1.2.1637330894.1594635482; tz=Asia%2FSingapore; _device_id=cbbd72bf5ce824f123f2dfa8e6b0797d; user_session=FULeJ3UzYYoWUbkq3AYJH_kXtW--S1b2YzDk0lyV9HVza8AB; __Host-user_session_same_site=FULeJ3UzYYoWUbkq3AYJH_kXtW--S1b2YzDk0lyV9HVza8AB; dotcom_user=leyonglin; has_recent_activity=1; _gat=1; _octo=GH1.1.1326980601.1594931725; logged_in=no; _gh_sess=FGjsXoGOiB9JZu5IyOS0iu2FJSIgjtqvMUVHgRB1IObUeIOtuuPJDCFQuAzINWo5RJXE042Xv5O3wtIiWmC8CkAmFcVqK63pGFNlLucZKmTMKtieNMC6Dhy5oKCkkjtzQD2Mr4gjoKhyd144Wy2tkqE17JR5Vte3SP7gI33aurWWrcZaNH3%2Fx3NVBvlWwBNt3CgRh1IgHVmSZHTawJ919ggHP3J9a0BLlKrZj5p9BAj9CqQ0y%2F4nA7BfhjzkGsyH0S1taBUSNRYqS%2Ftdmx7hsIqnlQGqXL047k9omOK64fAjmmt3--1YhDlDoyAz6ErhnD--r%2FLI1uaGC8QELLskWBX%2Buw%3D%3D'

#cookie_list = Cookie_temp.split('; ')
#cookies = {cookie.split('=')[0]: cookie.split('=')[-1]for cookie in cookie_list}
#print(cookies)
#response=requests.get(url, headers=headers, cookies=cookies)

response=requests.get(url)
print(len(response.content.decode()))

response1=requests.get(url, headers=headers)
print(len(response1.content.decode()))


####################### param ################################

url="http://www.baidu.com/s?"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

params = {
    'wd': 'python'
}

# timeout超时为3秒 ， verify不进行ca证书认证(有些网站证书过期但是点高级还是能使用)
response=requests.get(url, headers=headers, params=params, timeout=3, verify=False)

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



