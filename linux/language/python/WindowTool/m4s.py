import os
import subprocess
import requests
from lxml import etree
import json
import re
requests.packages.urllib3.disable_warnings()


class Bilibili():
    def __init__(self,index_url,storage_dir):
        self.storage_dir = storage_dir
        self.index_url = index_url
        self.headers = {
            'Origin': 'https://www.bilibili.com',
            # Range: bytes=331501-396520,
            # 'Referer': 'https://www.bilibili.com/video/BV16K4y1b787?p=7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

    # 获取每集名称
    def get_name(self):
        # 获取首页源码
        index_response = requests.get(self.index_url, headers=self.headers).content.decode()

        #创建lxml
        index_html = etree.HTML(index_response)

        self.create_dir(index_html)
        # 获取数据列表
        index_info = index_html.xpath('//script')
        name_lxml = index_info[6].xpath('./text()')[0]
        name_str = name_lxml[25:]
        name_str = re.match(r"(.*),\"subtitle", name_str).group(1)
        name_str = name_str + "}}"
        name_json = json.loads(name_str)
        name_json_list = name_json['videoData']['pages']
        name_list=[]
        for i in range(len(name_json_list)):
            name_list.append(name_json_list[i]['part'].replace(" ","-"))
        return name_list

    # 获取视频url
    def getVideoUrl(self,name_list):
        num = len(name_list)
        video_url_list = []
        audio_url_list = []
        homeurl_list = []
        for i in range(1,num+1):
            params = {
                "p":i
            }
            response = requests.get(self.index_url,params=params, headers=self.headers)
            response_html = etree.HTML(response.content.decode())
            index_info = response_html.xpath('//script')
            video_lxml = index_info[5].xpath('./text()')[0]
            video_str = str(video_lxml)[20:]
            video_json = json.loads(video_str)
            video_url = video_json['data']['dash']['video'][0]['baseUrl']
            audeo_url = video_json['data']['dash']['audio'][0]['baseUrl']
            homeurl = response.url
            video_url_list.append(video_url)
            audio_url_list.append(audeo_url)
            homeurl_list.append(homeurl)

        info = {"name_list":name_list,"video_url_list":video_url_list,"audio_url_list":audio_url_list,'homeurl_list':homeurl_list}
        return info

    # 下载视频段
    def GetBiliVideo(self,info,udnum_list):
        name_list = info['name_list']
        video_url_list = info['video_url_list']
        audio_url_list = info['audio_url_list']
        homeurl_list = info['homeurl_list']
        if len(udnum_list):
            final_num_list = udnum_list
        # 总集数
        else:
            final_num_list = []
            num = len(name_list)
            for i in range(1, num + 1):
                final_num_list.append(i)
        result_list = []
        for i in final_num_list:
            #下载视频
            homeurl = homeurl_list[i]
            name_video_absolute = self.storage_dir + name_list[i] + "video" + ".m4s"
            print(name_video_absolute)
            video_url = video_url_list[i]
            self.download(name_video_absolute,video_url,homeurl)

            # 下载音频
            name_audio_absolute = self.storage_dir + name_list[i] + "audio" + ".m4s"
            print(name_audio_absolute)
            audio_url = audio_url_list[i]
            print(audio_url)
            self.download(name_audio_absolute,audio_url,homeurl)

            result = self.merge(name_video_absolute,name_audio_absolute,name_list[i])
            result_list.append(result)
        return result_list

    def download(self,absolute_path,url,homeurl):
        self.headers.update({'Referer': homeurl})
        res = requests.get(url=url, headers=self.headers, verify=False, stream=True)
        print(res.headers)
        content_size = int(re.split(r'[ /]', res.headers['Content-Length'])[-1])
        size = str(content_size / 1024 / 1024) + "Mb"
        print("文件大小：%s" % size)
        download_size = 0
        chunk_size = 1024
        with open(absolute_path, 'wb') as fp:
            for chunk in res.iter_content(chunk_size=chunk_size):
                if chunk:
                    fp.write(chunk)
                    download_size += chunk_size
                    print("\r", "下载进度: %.2f%s" % (download_size / content_size * 100, "%"), end='', flush=False)


    # 合并视频
    def merge(self,name_video_absolute,name_audio_absolute,name):
        ffmpeg = "D:/vmware-mount/windows/ffmpeg-4.3-win64-static/bin/ffmpeg"
        cmd = ffmpeg
        name = name + ".mp4"
        cmd = cmd + ' -threads 10' + " -i " + name_video_absolute + " -i " + name_audio_absolute + " -acodec copy" + " " + self.storage_dir + name
        print("\ncmd：%s" % cmd)
        logfile = self.storage_dir + 'log.txt'
        print('开始合并')
        f = open(logfile, 'w')
        result = subprocess.call(cmd, shell=True,stdout=f,stderr=f)
        f.close()
        print("merge ok")
        self.del_m4s(name_video_absolute,name_audio_absolute)
        return result

    # 获取标题(可作为文件夹的名称）
    def create_dir(self,html):
        # dirname = str(html.xpath("//h1/@title")[0].encode('ISO-8859-1').decode('utf-8'))
        dirname = str(html.xpath("//h1/@title")[0])
        dirname = self.storage_dir + dirname
        print(dirname)
        if not os.path.exists(dirname):
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(dirname)
            print('目录文件创建成功!，\033[30;41m请注意防止名称有特殊字符\033[0m')
        else:
            print('\033[30;41m目录已存在，请检查是否重复\033[0m')
            # exit(-1)
        self.storage_dir = dirname + '/'


    # 删除视频段
    def del_m4s(self,name_video,name_audio):
        # window路径容易有特殊含义字符(如v开头的在合成路径就变成\v，就是特殊字符)
        # os.chdir(self.storage_dir)
        print("删除视频段 %s %s" % (name_video,name_audio))
        os.remove(name_video)
        os.remove(name_audio)

    # 处理集数问题
    @staticmethod
    def deal_num(userdefind_range):
        if userdefind_range=='' or userdefind_range==' ':
            return []
        num_list = []
        for i in (re.split(r'[ ,]', userdefind_range)):
            try:
                # 转换成人类可读的集数，机器是从0开始的
                num_list.append(int(i)-1)
            except ValueError:
                numlist = re.split(r'[-]', i)
                start = int(numlist[0])
                end = int(numlist[1]) + 1
                for i in range(start, end):
                    num_list.append(int(i)-1)
        return num_list



if __name__ == '__main__':
    storage_dir = "D:/spider/video/m4s/"
    index_url = "https://www.bilibili.com/video/BV16K4y1b787"
    # 视频选集，空表示下载所有
    userdefind_range = '6-7'
    udnum_list = Bilibili.deal_num(userdefind_range)
    bilibili = Bilibili(index_url,storage_dir)
    name_list = bilibili.get_name()
    info = bilibili.getVideoUrl(name_list)
    result = bilibili.GetBiliVideo(info,udnum_list)
    print(result)