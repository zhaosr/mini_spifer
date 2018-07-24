#_*_ coding:utf-8 _*_
import urllib2
import re


class Spider():
    """
    内涵段子吧的一个小爬虫
    """
    def __init__(self):
        self.enable = True
        self.page = 1

    def load_page(self, page):
        url = 'https://www.neihan8.com/article/list_5_'+ str(page) +'.html'

        user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

        headers = {"User-Agent":user_agent}

        req = urllib2.Request(url,headers = headers)

        response = urllib2.urlopen(req)

        html = response.read()

        new_html = html.decode('gbk').encode('utf-8')

        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)

        item_list = pattern.findall(new_html)
        return item_list

    def deal_one_page(self, item_list, page):
        """处理一页的数据"""
        print("************第%d页的数据************" % page)
        for item in item_list:
            self.write_file(item)
        print("************第%d页的数据写入文件完毕************" % page)

    def write_file(self,txt):
        f = open('myStory.txt','a')
        f.write(txt)
        f.write('-------------')
        f.close()

    def do_work(self):
        """提供一个跟用户交互的过程"""
        while self.enable:
            print("按回车继续")
            print("按q退出")
            command = raw_input()
            if (command == "q"):
                self.enable = False
                break
            item_list = self.load_page(self.page)
            self.deal_one_page(item_list,self.page)
            self.page += 1


if __name__ == '__main__':
    myspider = Spider()
    myspider.do_work()
