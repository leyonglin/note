import requests
from lxml import etree

class Tieba():
    def __init__(self,name):
        self.url = "https://tieba.baidu.com/f?kw={}".format(name)
        # 调试url
        # print(self.url)
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        #确保能获取数据
        # with open("tieba.html","wb") as f:
        #     f.write(response.content)
        return response.content

    def parse_data(self,data):
        #因为目标代码被注释，xpath无法匹配到(浏览器是因为浏览器引擎能渲染)
        data = data.decode().replace("<!--","").replace("-->","")
        html = etree.HTML(data)
        #google浏览器，在目标处右键"检查",再右键copy--copy xpath能复制xpath，再进行修改
        el_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # 显示获取结果
        # print(len(el_list))

        #提取数据
        data_list = []
        for el in el_list:
            temp = {}
            #默认是列表，需要的是字符串数据
            temp['title'] = el.xpath('./text()')[0]
            # print(temp['title'])
            temp['link'] = 'https://tieba.baidu.com' + el.xpath('./@href')[0]
            # print(temp['link'])
            data_list.append(temp)

        #下一页，不要用索引，因为是动态的
        try:
            #xpath有多种匹配方式，有时候某种方式在浏览器可以匹配但在程序中会有bug，换一种就好了
            # next_url = 'https:' + html.xpath('//a[@class="next pagination-item"]/@href')[0]
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页>")]/@href')[0]
        except:
            next_url = None

        return data_list,next_url

    def save_data(self,data_list):
        for data in data_list:
            print(data)

    def run(self):
        next_url = self.url
        while True:
            #发送请求，获取响应
            data = self.get_data(next_url)
            #从响应中提取数据(数据和翻页用的url)
            data_list,next_url = self.parse_data(data)
            # print(data_list)
            # print(next_url)
            #数据保存
            self.save_data(data_list)
            #判断是否终结
            if next_url is None:
                break


if __name__ == '__main__':
    tieba=Tieba("传智播客")
    tieba.run()

