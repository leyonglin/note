# import os
# import subprocess
# from multiprocessing import Pool
# import requests
# from lxml import etree
# import json
# import re
# # 防止因https证书问题报错
# requests.packages.urllib3.disable_warnings()
#
# # 216状态码：客户端通过发送范围请求头Range抓取到了资源的部分数据  header格式：Range: bytes=3061232-3433459
# # 406状态码：所请求的范围无法满足 (Requested Range not satisfiable) 即：Range: bytes=3061232-3433459
# # m4s视频格式的只要找到音视频的url，可以直接下载全部内容，也可以分段下载
#
# class Bilibili():
#     def __init__(self,index_url,storage_dir):
#         self.storage_dir = storage_dir
#         self.index_url = index_url
#         self.headers = {
#             'Origin': 'https://www.bilibili.com',
#             # Range: bytes=331501-396520,
#             # 'Referer': 'https://www.bilibili.com/video/BV16K4y1b787?p=7',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#         }
#
#     # 获取每集名称
#     def get_name(self):
#         # 获取首页源码
#         index_response = requests.get(self.index_url, headers=self.headers).content.decode()
#
#         #创建lxml
#         index_html = etree.HTML(index_response)
#
#         self.create_dir(index_html)
#         # 获取数据列表
#         index_info = index_html.xpath('//script')
#
#         # 这里要确定是什么顺序，好像会随时变动
#         # print(len(index_info))
#         # for i in range(len(index_info)):
#         #     print(index_info[i].xpath('./text()'))
#         # 匹配名称
#         # 匹配到window.__INITIAL_STATE__=
#         name_lxml = index_info[6].xpath('./text()')[0]
#         # print(name_lxml)
#         # 变成字符串
#         # 去头
#         name_str = name_lxml[25:]
#         # print(name_str)
#         # 去尾
#         # name_str = re.findall('(.*),"subtitle',name_str)
#         name_str = re.match(r"(.*),\"subtitle", name_str).group(1)
#         # 使用字符串在json.cn可以解析
#         name_str = name_str + "}}"
#         # 转成字符串在json.cn不可以解析，但python获取数据需要
#         name_json = json.loads(name_str)
#         name_json_list = name_json['videoData']['pages']
#         # print(name_json_list)
#         name_list=[]
#         for i in range(len(name_json_list)):
#             # 如果名称有特殊字符可以替换掉，这里的特殊字符是空格
#             name_list.append(name_json_list[i]['part'].replace(" ","-"))
#         # print(name_list)
#         return name_list
#
#     # 获取视频url
#     def getVideoUrl(self,name_list):
#         # 总集数
#         num = len(name_list)
#         video_url_list = []
#         audio_url_list = []
#         homeurl_list = []
#         for i in range(1,num+1):
#             params = {
#                 "p":i
#             }
#             response = requests.get(self.index_url,params=params, headers=self.headers)
#             # print(response.url)
#
#             # 音视频路径：匹配到window.__playinfo__=
#             response_html = etree.HTML(response.content.decode())
#             index_info = response_html.xpath('//script')
#             video_lxml = index_info[5].xpath('./text()')[0]
#             # print(video_lxml)
#             # 变成字符串
#             ## 使用字符串在json.cn可以解析
#             video_str = str(video_lxml)[20:]
#
#             # 过滤出需要的json数据
#             # 转成字符串在json.cn不可以解析，但python获取数据需要
#             video_json = json.loads(video_str)
#             # 获取视频的清晰度列表，可以根据清晰度进行过滤，这里不进行筛选，直接
#             # accept_description = video_json['data']['accept_description']
#             # accept_quality = video_json['data']['accept_quality']
#             # for i in zip(accept_description,accept_quality):
#             #     print(i)
#
#             video_url = video_json['data']['dash']['video'][0]['baseUrl']
#             audeo_url = video_json['data']['dash']['audio'][0]['baseUrl']
#             homeurl = response.url
#             video_url_list.append(video_url)
#             audio_url_list.append(audeo_url)
#             homeurl_list.append(homeurl)
#
#         info = {"name_list":name_list,"video_url_list":video_url_list,"audio_url_list":audio_url_list,'homeurl_list':homeurl_list}
#         # print(info)
#         return info
#
#     # 下载视频段
#     def GetBiliVideo(self,info,udnum_list):
#         name_list = info['name_list']
#         # print(name_list)
#         video_url_list = info['video_url_list']
#         # print(video_url_list)
#         audio_url_list = info['audio_url_list']
#         # print(audio_url_list)
#         homeurl_list = info['homeurl_list']
#         # print(homeurl_list)
#         if len(udnum_list):
#             num = len(udnum_list)
#             final_num_list = udnum_list
#         # 总集数
#         else:
#             final_num_list = []
#             num = len(name_list)
#             for i in range(1, num + 1):
#                 final_num_list.append(i)
#         result_list = []
#         for i in final_num_list:
#             #下载视频
#             homeurl = homeurl_list[i]
#             name_video_absolute = self.storage_dir + name_list[i] + "video" + ".m4s"
#             print(name_video_absolute)
#             video_url = video_url_list[i]
#             # print(video_url)
#             self.download(name_video_absolute,video_url,homeurl)
#             # video = requests.get(video_url).content
#             # with open(name_video_absolute,"wb")as f:
#             #     f.write(video)
#
#             # 下载音频
#             name_audio_absolute = self.storage_dir + name_list[i] + "audio" + ".m4s"
#             print(name_audio_absolute)
#             audio_url = audio_url_list[i]
#             print(audio_url)
#             self.download(name_audio_absolute,audio_url,homeurl)
#             # audio_content = requests.get(audio_url).content
#             # with open(name_audio_absolute, "wb")as f:
#             #     f.write(audio_content)
#
#             result = self.merge(name_video_absolute,name_audio_absolute,name_list[i])
#             result_list.append(result)
#         return result_list
#
#     def download(self,absolute_path,url,homeurl):
#         # 修改headers
#         self.headers.update({'Referer': homeurl})
#         # 好像不用也可以，在获取b站视频之前需要用OPTION方式向请求服务器分配资源，然后再用GET方式获取视频分片
#         # requests.options(url=url, headers=self.headers, verify=False)
#         # m4s格式的只要找到音视频的url，可以直接下载全部内容，并且不用上面options请求
#         # 每次下载1M的数据
#         # begin = 0
#         # end = 1024 * 512 - 1
#         # flag = 0
#         # while True:
#         #     # print(begin,end)
#         #     self.headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
#         #     # print("Range: bytes= %s %s" % (str(begin),str(end)))
#         #     res = requests.get(url=url, headers=self.headers, verify=False, stream=True)
#             # print(res.headers['Content-Range'])
#             # print(type(res.headers['Content-Range']))
#             # exit()
#
#             # 第一种方法是利用响应状态码
#             # if res.status_code != 406:
#             #     begin = end + 1
#             #     end = end + 1024 * 512
#             # else:
#             #     # 发生406说明range不对，那么直接不要结束range就行，也说明资源已下载完毕
#             #     self.headers.update({'Range': str(end + 1) + '-'})
#             #     res = requests.get(url=url, headers=self.headers, verify=False)
#             #     flag = 1
#
#             # 第二种是利用响应头已字段已给出大小
#             # size = int(re.split(r'[ /]', res.headers['Content-Range'])[-1])
#             # # print(size)
#             # if end < size - 1024 * 512:
#             #     begin = end + 1
#             #     end = end + 1024 * 512
#             # else:
#             #     # 发生406说明range不对，那么直接不要结束range就行，也说明资源已下载完毕
#             #     self.headers.update({'Range': str(end + 1) + '-' + str(size-5)})
#             #     # print("Range: bytes= %s %s aaaaaa" % (str(end + 1),str(size)))
#             #     res = requests.get(url=url, headers=self.headers, verify=False, stream=True)
#             #     # print(res.headers['Content-Range'])
#             #     flag = 1
#             # with open(absolute_path, 'ab') as fp:
#             #     # 这里一直卡住了
#             #     fp.write(res.content)
#             #     fp.flush()
#             #
#             # # data=data+res.content
#             # if flag == 1:
#             #     fp.close()
#             #     break
#         
#         # 断点下载
#         # 文件总大小
#         r1 = requests.get(url, stream=True, verify=False)
#         total_size = int(r1.headers['Content-Length'])
#         # 本地文件下载了多少
#         if os.path.exists(file_path):
#             temp_size = os.path.getsize(file_path)  # 本地已经下载的文件大小
#         else:
#             temp_size = 0
#         # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载，追加到文件中去
#         headers = {'Range': 'bytes=%d-' % temp_size}  
#    
#         # 下载大文件方法  
#         res = requests.get(url=url, headers=self.headers, verify=False, stream=True)
#         print(res.headers)
#         content_size = int(re.split(r'[ /]', res.headers['Content-Length'])[-1])
#         size = str(content_size / 1024 / 1024) + "Mb"
#         print("文件大小：%s" % size)
#         download_size = 0
#         chunk_size = 1024
#         with open(absolute_path, 'wb') as fp:
#             for chunk in res.iter_content(chunk_size=chunk_size):
#                 if chunk:
#                     fp.write(chunk)
#                     download_size += chunk_size
#                     # 覆盖，不换行输出
#                     print("\r", "下载进度: %.2f%s" % (download_size / content_size * 100, "%"), end='', flush=False)
#
#
#     # 合并视频
#     def merge(self,name_video_absolute,name_audio_absolute,name):
#         ffmpeg = "D:/vmware-mount/windows/ffmpeg-4.3-win64-static/bin/ffmpeg"
#         cmd = ffmpeg
#         name = name + ".mp4"
#         # 不用多线程操作特别慢
#         cmd = cmd + ' -threads 10' + " -i " + name_video_absolute + " -i " + name_audio_absolute + " -acodec copy" + " " + self.storage_dir + name
#         print("cmd %s" % cmd)
#         # 将命令执行结果输出到文件中
#         f = open('log.txt', 'w')
#         # 0为正确执行，1为错误执行,call表示同步执行，Popen表示异步执行
#         result = subprocess.call(cmd, shell=True,stdout=f,stderr=f)
#         f.close()
#         print("merge ok")
#         self.del_m4s(name_video_absolute,name_audio_absolute)
#         return result
#
#     # 获取标题(可作为文件夹的名称）
#     def create_dir(self,html):
#         # dirname = str(html.xpath("//h1/@title")[0].encode('ISO-8859-1').decode('utf-8'))
#         dirname = str(html.xpath("//h1/@title")[0])
#         dirname = self.storage_dir + dirname
#         print(dirname)
#         if not os.path.exists(dirname):
#             # 如果不存在则创建目录
#             # 创建目录操作函数
#             os.makedirs(dirname)
#             print('目录文件创建成功!，\033[30;41m请注意防止名称有特殊字符\033[0m')
#         else:
#             print('\033[30;41m目录已存在，请检查是否重复\033[0m')
#             # exit(-1)
#         self.storage_dir = dirname + '/'
#
#
#     # 删除视频段
#     def del_m4s(self,name_video,name_audio):
#         # window路径容易有特殊含义字符(如v开头的在合成路径就变成\v，就是特殊字符)
#         # os.chdir(self.storage_dir)
#         print("删除视频段 %s %s" % (name_video,name_audio))
#         os.remove(name_video)
#         os.remove(name_audio)
#
#     # 处理集数问题
#     @staticmethod
#     def deal_num(userdefind_range):
#         if userdefind_range=='' or userdefind_range==' ':
#             return []
#         num_list = []
#         for i in (re.split(r'[ ,]', userdefind_range)):
#             try:
#                 # 转换成人类可读的集数，机器是从0开始的
#                 num_list.append(int(i)-1)
#             except ValueError:
#                 numlist = re.split(r'[-]', i)
#                 start = int(numlist[0])
#                 end = int(numlist[1]) + 1
#                 for i in range(start, end):
#                     num_list.append(int(i)-1)
#         return num_list
#
#
#
# if __name__ == '__main__':
#     storage_dir = "D:/spider/video/m4s/"
#     index_url = "https://www.bilibili.com/video/BV16K4y1b787"
#     # 视频选集，空表示下载所有
#     userdefind_range = '6-7'
#     udnum_list = Bilibili.deal_num(userdefind_range)
#     bilibili = Bilibili(index_url,storage_dir)
#     name_list = bilibili.get_name()
#     info = bilibili.getVideoUrl(name_list)
#     result = bilibili.GetBiliVideo(info,udnum_list)
#     print(result)

#########################################################################



# m3u8视频格式的有一个m3u8文件，里面记录着请求分段视频内容的url地址
# 有的视频可能会遇到加密的情况，一般是有一个单独的 key 文件存在，而在 m3u8 文件中，也会存在一个 key 引用的内容

import multiprocessing
import os
import time
import requests
import json
import re

from lxml import etree


class JiQiMao():
    def __init__(self,detail_url,storage_dir):
        # 这个url是根据观察来的，是在一个js文件中
        self.parse_url = "http://apick.jiqimao.tv/service/ckplayer/parser/"
        self.storage_dir = storage_dir
        # 显示集数的url
        self.detail_url = detail_url
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                    }

    # 获取电视剧集数列表
    def get_detail_message(self):
        response = requests.get(self.detail_url,headers=self.headers)
        # 创建html对象
        detail_html = etree.HTML(response.content.decode())
        # 获取的是个每集url列表
        home_url_list = detail_html.xpath('//div[@data-group="ttp_vid_zuida"]//li/a/@href')
        # 需要获取每个视频名称列表video_name_list
        video_name_list = detail_html.xpath('//div[@data-group="ttp_vid_zuida"]//li/a/@title')
        
        detail_message = {"home_url_list":home_url_list,"video_name_list":video_name_list}
        return detail_message

    # 获取m3u8文件
    def get_m3u4_url(self, home_url):
        # 构建m3u8的get请求参数
        params = {
            "jsonpcallback": "jiqimao_jsoncallback" + str(int(time.time() * 1000)),
            "sid": home_url.split("/")[-1],
            "type": "1",
            "mode": "pc",
            "_": int(time.time() * 1000) + 62
        }
        # print(params)
        
        self.headers["Referer"] = home_url
        # 请求含有m3u8路径的响应
        response = requests.get(self.parse_url, params=params, headers=self.headers)

        # with open("lianaixiansheng.html","wb")as f:
        #     f.write(response.content.decode())
        # print(response.content.decode())

        # 过滤响应数据
        data = response.content.decode()[34:-1]
        # print(data)

        # 转换成字典
        data_json = json.loads(data)
        # print(data_json)

        # 第一个m3u8文件路径
        m3u8_url = data_json["data"]["parser"]["url"]

        # m3u8存放的是相对于当前的相对路径
        relative_url = "/".join(m3u8_url.split("/")[:-1])

        # 第一个m3u8文件的内容
        response = requests.get(m3u8_url, headers=self.headers).content.decode()

        # 文件内容仍是m3u8文件路径，继续请求
        re_m3u8 = re.findall(".*m3u8", response)[0]
        if re_m3u8:
            # 这是最终包含ts路径的m3u8的url
            m3u8_url = relative_url + "/" + re_m3u8
            response = requests.get(m3u8_url, headers=self.headers).content.decode()

        # 继续补全当前路径
        relative_url = relative_url + "/" + "/".join(re_m3u8.split("/")[:-1])

        # 获取ts相对路径列表
        ts_url_list = re.findall(".*ts", response)

        # 过滤掉开头
        ts_url_list = ts_url_list[22:]
        # 过滤掉结尾
        ts_url_list = ts_url_list[:-38]

        data = {"relative_url":relative_url,"ts_url_list":ts_url_list}
        # print(data)
        return data

    # 获取完整的ts列表
    def get_ts(self,data):
        relative_url = data["relative_url"]
        ts_url_list = data["ts_url_list"]
        finish_ts_url = []
        for i in ts_url_list:
            ts_url = relative_url + "/" + i
            finish_ts_url.append(ts_url)
        # print(finish_ts_url)
        return finish_ts_url

    # 采用进程池多进程下载
    #单线程
    # def func(args):
    #      for i in range(100):
    #          print(i)
    #多线程
    # def func(args):
    #   print(args)
    # if __name__ == "__main__":
    #    p = multiprocessing.Pool(5)
    #    p.map(func, range(100))
    #等待上面子进程执行完成再继续执行主进程
    #    print("finish")
    ###################################
    #from multiprocessing import Queue, Process, Pool
	#import os
	#def test():
	#    time.sleep(2)
	#    print('this is process {}'.format(os.getpid()))
	#    print("2miao")
	#
	#def test1():
	#    time.sleep(5)
	#    print('this is process {}'.format(os.getpid()))
	#    print("5miao")
	#
	#
	#def get_pool(n=5):
	#    p = Pool(n) # 设置进程池的大小
	#    p.apply_async(test)
	#    p.apply_async(test1)
	#    p.close() # 关闭进程池
	#    p.join()  #等待上面子进程执行完成再继续执行主进程
	#
	#if __name__ == '__main__':
	#    print(time.time())
	#    get_pool()
	#    print('ths process is ended')
	#    print(time.time())
    def download_ts(self,data):
        content = requests.get(data,headers=self.headers)
        file_name = data.split("/")[-1]
        print(self.storage_dir+file_name)
        with open(self.storage_dir+file_name,"wb")as f:
            f.write(content.content)

    # 视频合并，但视频片太多了，导致参数过长
    # def ffmpeg_video(self,data):
    #     ffmpeg = "D:/vmware-mount/windows/ffmpeg-4.3-win64-static/bin/ffmpeg"
    #     cmd = ffmpeg
    #     for i in data:
    #         cmd += " -i "
    #         cmd += self.storage_dir + i.split("/")[-1]
    #     cmd = cmd + " -acodec copy" + " " + self.storage_dir + "finish.mp4"
    #     print(cmd)
    #     result = subprocess.call(cmd, shell=True)  # 调用shell命令
    #     print(type(result))
    #     print(result)

    # 采用文件追加方式进行ts视频段合并
    def video_merge(self,data,video_name):
        # dir = "D:/spider/video/spider_m3u8/part"
        ts_url_list = data["ts_url_list"]
        for i in ts_url_list:
            # print(i)
            f1 = open(self.storage_dir + i, "rb")
            content = f1.read()
            with open(self.storage_dir + video_name+ ".mp4", "ab") as mon:
                mon.write(content)
            f1.close()
    
    # 删除ts视频片
    def del_ts(self,data):
        ts_url_list = data["ts_url_list"]
        for i in ts_url_list:
            os.remove(self.storage_dir + i)



if __name__ == '__main__':
    storage_dir = "D:/spider/video/spider_m3u8/part/"
    detail_url = "http://jiqimao.tv/movie/show/fbd913b96b6111b76aeeb865a190247662a7dfb5"
    jixiaolan = JiQiMao(detail_url,storage_dir)
    detail_message = jixiaolan.get_detail_message()
    home_url_list = detail_message["home_url_list"]
    video_name_list = detail_message["video_name_list"]
    # print(video_name_list[0][:-4])
    # print(home_url_list)
    # 遍历，获取每一集对应的url ,可以在这里指定一个集数列表    
    # for i in range(15, 22):     #16-22集
    # a = [14,17]  # 15集 和 18集 
    for i in range(len(home_url_list)):
        # print(home_url)
        data = jixiaolan.get_m3u4_url(home_url_list[i])
        # print(data)
        finish_ts_url = jixiaolan.get_ts(data)
        # print(finish_ts_url)
        # break
        # 下载采用线程池进行多线程下载
        p = multiprocessing.Pool(10)
        p.map(jixiaolan.download_ts, finish_ts_url)
        print("download finish")
        jixiaolan.video_merge(data,video_name_list[i][:-4])
        print("video merge %s ok" % video_name_list[i][:-4])
        #合并完视频段删除ts文件
        jixiaolan.del_ts(data)
        print("ts del %s ok" % video_name_list[i][:-4])
        



