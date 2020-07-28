# import requests
# from lxml import etree
# import json
# import re
#
#
# # 1.Ctrl+Shift+C 是查看指定区域html代码的快捷键，但是查看到视频位置的链接为加密链接，无法直接访问
# # 抓包，查看视频片，及视频片的来源，来源发现来自主页
#
# index_url = "https://www.bilibili.com/video/av26019104"
#
# index_header = {
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
#     }
#
# #获取主页html代码
# index_response = requests.get(index_url,headers=index_header)
#
# # print(index_response.status_code)
# #
# # with open("index.html","wb")as f:
# #     f.write(index_response.content)
#
# #过滤出想要的数据
# index_html = etree.HTML(index_response.content.decode())
# index_info = index_html.xpath('/html/head/script[3]/text()')[0]
#
#
# # loads将字符串转换成字典，对数据进行提取
# index_json = json.loads(re.findall("{.*}",index_info)[0])
#
#
# #下载视频
# video_url = index_json["data"]["dash"]["video"][0]["baseUrl"]
# # print(video_url)
# # video_content = requests.get(video_url,headers=index_header)
# # with open("video.mp4","wb")as f:
# #     f.write(video_content.content)
#
# #下载音频
# audio_url = index_json["data"]["dash"]["audio"][0]["baseUrl"]
# # print(audio_url)
# # audio_content = requests.get(audio_url,headers=index_header)
# # with open("audio.mp4","wb")as f:
# #     f.write(audio_content.content)



#########################################################################



# # 216状态码：客户端通过发送范围请求头Range抓取到了资源的部分数据  header格式：Range: bytes=3061232-3433459
# # 406状态码：所请求的范围无法满足 (Requested Range not satisfiable) 即：Range: bytes=3061232-3433459
# # m4s视频格式的只要找到音视频的url，可以直接下载全部内容，也可以分段下载
#
#
# # 参考链接：https://segmentfault.com/a/1190000021645432
# import requests
# import json
# from lxml import etree
# #ffmpeg是一个工具，用来处理音视频数据(转换合并等)
# import ffmpeg.video
# import os
# import subprocess
#
# # 防止因https证书问题报错
# requests.packages.urllib3.disable_warnings()
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
#     'Referer': 'https://www.bilibili.com/'
# }
#
#
# def GetBiliVideo(homeurl,num,session=requests.session()):
#     #获取首页数据，不进行tls认证
#     res = session.get(url=homeurl, headers=headers, verify=False)
#     html = etree.HTML(res.content)
#     # 提取视频数据，[20:]表示字符串截取
#     videoinforms = str(html.xpath('//head/script[3]/text()')[0])[20:]
#     # loads将字符串转换成字典，对数据进行提取
#     videojson = json.loads(videoinforms)
#     # 获取详情信息列表
#     #listinform = str(html.xpath('//head/script[4]/text()')[0])
#     listinform = str(html.xpath('//head/script[4]/text()')[0].encode('ISO-8859-1').decode('utf-8'))[25:-122]
#     listjson=json.loads(listinform)
#     # 获取视频链接和音频链接
#     try:
#         # 音频AudioURl和视频VideoURL分离
#         VideoURL = videojson['data']['dash']['video'][0]['baseUrl']
#         AudioURl = videojson['data']['dash']['audio'][0]['baseUrl']
#         flag=0
#     except Exception:
#         # 2018年以前的b站视频，格式为flv
#         VideoURL = videojson['data']['durl'][0]['url']
#         flag=1
#     # 获取标题(可作为文件夹的名称）
#     dirname = str(html.xpath("//h1/@title")[0].encode('ISO-8859-1').decode('utf-8'))
#     if not os.path.exists(dirname):
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(dirname)
#         print('目录文件创建成功!')
#     # 获取每一集的名称
#     name=listjson['videoData']['pages'][num]['part']
#     print(name)
#     # 下载视频和音频
#     print('正在下载 "'+name+'" 的视频····')
#     BiliBiliDownload(homeurl=homeurl,url=VideoURL, name=os.getcwd()+'/'+dirname+'/'+name + '_Video.mp4', session=session)
#     if flag==0:
#         print('正在下载 "'+name+'" 的音频····')
#         BiliBiliDownload(homeurl=homeurl,url=AudioURl, name=os.getcwd()+'/'+dirname+'/'+name+ '_Audio.mp3', session=session)
#         print('正在组合 "'+name+'" 的视频和音频····')
#     # CombineVideoAudio(name + '_Video.mp4',name + '_Audio.mp3',name + '_output.mp4')
#     print(' "'+name+'" 下载完成！')
#
# def BiliBiliDownload(homeurl,url, name, session=requests.session()):
#     #修改headers
#     headers.update({'Referer': homeurl})
#     # 好像不用也可以，在获取b站视频之前需要用OPTION方式向请求服务器分配资源，然后再用GET方式获取视频分片
#     session.options(url=url, headers=headers,verify=False)
#     # m4s格式的只要找到音视频的url，可以直接下载全部内容，并且不用上面options请求
#     # 每次下载1M的数据
#     begin = 0
#     end = 1024*512-1
#     flag=0
#     while True:
#         headers.update({'Range': 'bytes='+str(begin) + '-' + str(end)})
#         res = session.get(url=url, headers=headers,verify=False)
#         if res.status_code != 416:
#             begin = end + 1
#             end = end + 1024*512
#         else:
#             # 发生406说明range不对，那么直接不要结束range就行，也说明资源已下载完毕
#             headers.update({'Range': str(end + 1) + '-'})
#             res = session.get(url=url, headers=headers,verify=False)
#             flag=1
#         with open(name, 'ab') as fp:
#             fp.write(res.content)
#             fp.flush()
#
#         # data=data+res.content
#         if flag==1:
#             fp.close()
#             break
#
# def CombineVideoAudio(videopath,audiopath,outpath):
#     ffmpeg.video.combine_audio(videopath,audiopath,outpath)
#     os.remove(videopath)
#     os.remove(audiopath)

# # 自定义抓换音视频
# # def combine_audio(video_file, audiio_file, out_file):
# #     try:
# #         cmd ='D:/python/ffmpeg-20200115-0dc0837-win64-static/bin/ffmpeg -i '+video_file+' -i '+audiio_file+' -acodec copy '+out_file
# #         print(cmd)
# #         subprocess.call(cmd, shell=True)   # 调用shell命令
# #         print('Muxing Done')
# #         判断执行结果
# #         if res != 0:
# #             return False
# #         return True
# #     except Exception:
# #         return False
#
#
# if __name__ == '__main__':
#
#     # av44518113
#     av = input('请输入视频号：')
#     url='https://www.bilibili.com/video/'+av
#     # 视频选集
#     range_start=input('从第几集开始？')
#     range_end = input('到第几集结束？')
#     if int(range_start) <= int(range_end):
#         for i in range(int(range_start),int(range_end)+1):
#             GetBiliVideo(url+'?p='+str(i),i-1)
#     else:
#         print('选集不合法！')


#########################################################################



# m3u8视频格式的有一个m3u8文件，里面记录着请求分段视频内容的url地址
# 有的视频可能会遇到加密的情况，一般是有一个单独的 key 文件存在，而在 m3u8 文件中，也会存在一个 key 引用的内容

import multiprocessing
import subprocess
import time
import requests
import json
import re

from lxml import etree


class JiQiMao():
    def __init__(self,detail_url):
        # 这个url是根据观察来的，是在一个js文件中
        self.parse_url = "http://apick.jiqimao.tv/service/ckplayer/parser/"
        self.storage_dir = "C:/Users/bang/Desktop/nginx/spider_m3u8/part/"
        self.detail_url = detail_url
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                    }

    # 获取电视剧集数列表
    def get_home_url(self):
        response = requests.get(self.detail_url,headers=self.headers)
        #创建html对象
        detail_html = etree.HTML(response.content.decode())
        #获取的是个列表，这里只下载一集
        home_url = str(detail_html.xpath('//div[@data-group="ttp_vid_zuida"]//li/a/@href')[0])
        return home_url

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
        self.headers["Referer"] = home_url

        # 请求含有m3u8路径的响应
        response = requests.get(self.parse_url, params=params, headers=self.headers)

        # print(response.content.decode())

        # 过滤响应数据
        data = response.content.decode()[34:-1]

        # 转换成字典
        data_json = json.loads(data)

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
    def download_ts(self,data):
        content = requests.get(data,headers=self.headers)
        file_name = data.split("/")[-1]
        print(file_name)
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
    def video_merge(self,data):
        dir = "C:/Users/bang/Desktop/nginx/spider_m3u8/part/"
        ts_url_list = data["ts_url_list"]
        for i in ts_url_list:
            # print(i)
            f1 = open(dir + i, "rb")
            content = f1.read()
            with open(dir + "finish.mp4", "ab") as mon:
                mon.write(content)
            f1.close()


if __name__ == '__main__':
    jixiaolan = JiQiMao("http://jiqimao.tv/movie/show/6eea36203c98ba920c9871eefd45e16bb9db1ecf")
    home_url = jixiaolan.get_home_url()
    data = jixiaolan.get_m3u4_url(home_url)
    finish_ts_url = jixiaolan.get_ts(data)
    p = multiprocessing.Pool(10)
    p.map(jixiaolan.download_ts, finish_ts_url)
    print("download finish")
    jixiaolan.video_merge(data)
    print("video merge ok")

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




