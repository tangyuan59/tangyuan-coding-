import re
import os
import time
import json
import random
import pandas as pd
import requests
from lxml import etree
import random


# 请求头
headers = { "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
            #"Cookie" : "tapadid=d6caf29c-5887-f438-c5da-028c12719be7; _ga=GA1.2.1974921996.1596017450; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjVXYzE5U1NUNnBmS1dpNDV4R09SWEE9PSIsInZhbHVlIjoia3E5K3JpeWFFbWU4ZG03dTRyQWZzNlBrTU5rUVpDdTRFeGpJRFwvWW9lR3EySzJVTmVRdlhnTWlUQzFXUFg2dUxDUnVpNnI1dHhMRDdFSUJ6ZVwvcGpKMFc2a1VERHY4TGhZMzRlSUduVnFNcz0iLCJtYWMiOiI5OTZhNTkwYzc5MDBjZjBjMWNmYjdkMGQ0ZWMzNjFkMWJkNDM1ZDY1NDZmOTc0YThlYzFmNzgyOTEzZjg0ZmY2In0%3D; user_id=101719649; ACCOUNT_LOGGED_USER_FROM_WWW=thvryDKD02Zz3ZQ%2FszIXxg%3D%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22101719649%22%2C%22%24device_id%22%3A%221739a0d9d34afc-05ccaabf8280b2-3962430c-2073600-1739a0d9d35ad7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221739a0d9d34afc-05ccaabf8280b2-3962430c-2073600-1739a0d9d35ad7%22%7D; _gid=GA1.2.1501719794.1614565164; XSRF-TOKEN=eyJpdiI6Ik5MNDkxdzJtNkNEVDQ1SUtcL1VwbjhRPT0iLCJ2YWx1ZSI6InppdXBvTGNVUm5EK2dHR2tNaU1yWGt2WlM4OXBxUW1iTGZLT0drV052RVNEK0drRU1VNHpSbElcL3I2d3E0M1pFYkpRejJPVUMyNmFTNGFMMGZLZG94QT09IiwibWFjIjoiOTcxYmM3ZmQ5M2ZmYmZhZDE2MTk0ZTBiOTIyZTMwNDFiYTBmYzU5YWYxYzlkZTU1MTIzN2U1NjA2MzgxOWIyNCJ9; tap_sess=eyJpdiI6IlhnYjF4UndOUUdUdWdBeW5sNGFqSEE9PSIsInZhbHVlIjoiU1MrSlNaM0R4Z3FOSGE1dWVlQlIwSGlcL3BlZXZoeUdIQllyUll5ek5GNzZ6UnJUN2MwVm1RaTJXMUx0TXdaSG81R2Q3dUgrU0FLQTFndlBXd3ViRXd3PT0iLCJtYWMiOiI4MDRkZjNmNzRhNTAxYjViNWI1NWI3N2RlMzM4MjNkOGZlNzc1NGJjNTU2M2E3NGU0OTBhM2U0YTMwZmZmMWYzIn0%3D"
            }
# 代理ip
proxies= {'https':'221.5.80.66:3128'}


class tapspider(object):
    # 初始化
    def __init__(self,id,page):
        self.id = id
        self.page=page
        self.list = []
        for i in range(1,self.page):
            url = 'https://www.taptap.com/app/'+str(self.id)+'/topic?type=feed&sort=created&page='+str(i)
            request = requests.get(url, headers=headers)
            # xpath解析获取玩家详情页
            xpath_data = etree.HTML(request.content)
            # 获得用户帖子详情页
            playerid_url = xpath_data.xpath('//div[@class="common-v2-list topic-item common-box-card js-ugc-item js-moment-item"]/@href')
            self.list.extend(playerid_url)

     #解析网页
    # 解析用户帖子详情页
    def  parseplayer(self):
        # 创建对应列表储存对应数据
        name_list,create_time_list ,label_list ,play_time_list,title_list ,content_list ,img_list ,reply_list=[[] for i in range(8)]
        for  url  in  self.list:
            print(url)
            if 'topic' in url:
                request = requests.get(url, headers=headers, timeout=10)
                xpath_data = etree.HTML(request.content)
                # 玩家昵称
                try:
                    name = xpath_data.xpath('//div/a[@class="user-name "]/text()')[0]
                    name_list.append(name)
                except IndexError:
                    name = xpath_data.xpath('//div/div[@class="user-name-identity topic-author__app"]/a/text()')[0]
                    name_list.append(name)
                # 帖子创建时间
                create_time = xpath_data.xpath('//div/ul/li/span/text()')[0]
                create_time=create_time[0:10].replace('-', '/')
                create_time_list.append(create_time)

                # 帖子所属的分区
                label = xpath_data.xpath('//li[@class="topic-main_labels"]/a/text()')[0]
                label_list.append(label)
                    # 玩家游戏时间
                try:
                    playtime = xpath_data.xpath('//li/span[@class="text-score-time"]/text()')[0]
                    play_time_list.append(playtime)
                except:
                    play_time_list.append("")
                     # 帖子标题
                try:
                    title = xpath_data.xpath('//div[@class="top-title-author"]/./p/text()')[0].replace('\n', '')
                    title_list.append(title)
                except:
                    print(url, 'title')
                    # 帖子内容
                try:
                    content = xpath_data.xpath(
                         '//div/div[@class="bbcode-body bbcode-body-v2 js-open-bbcode-image js-translate-content"]//text()')
                    etmpy = ''
                    for text  in content:
                        etmpy= etmpy+' '+re.sub("(\s)|(\n)|(' ')|(,)",'',text)
                        content = etmpy
                    content_list.append(content)

                except:
                    print(url,'con')
                try:
                     # 图片链接
                    img = xpath_data.xpath('//div/div/img/@src')[2]
                    img_list.append(img)
                except:
                    print(url,'img')
                try:
                     # 回复
                    reply = xpath_data.xpath(
                         '//div/div/div[@class="item-text-body bbcode-body bbcode-body-v2 js-open-bbcode-image"]/text()')
                    reply_list.append(reply)
                except:
                    print(url,'re')
            else:
                #解析json
                if 'video' in url:
                    id = re.search('\d+',url).group()
                    user_url = 'https://www.taptap.com/webapiv2/video/v2/detail?id='+id+'&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D3%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D7d018504-3322-4788-8c64-024ea433da5d%26VID%3D345765606%26DT%3DPC'
                # 解析网址
                else:
                    id = re.search('\d+', url).group()
                    user_url = 'https://www.taptap.com/webapiv2/moment/v2/detail?id=' + id + '&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D3%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D7d018504-3322-4788-8c64-024ea433da5d%26VID%3D345765606%26DT%3DPC'
                    # 解析网
                request =requests.get(user_url)
                response = request.json()

                #用户昵称
                try:
                    name = response['data']['moment']['author']['user']['name']
                    name_list.append(name)
                except :
                    name= response['data']['video']['author']['name']
                    namelist.append(name_)

                # 帖子创建时间
                try:
                    create_time = response['data']['moment']['created_time']
                    time_local = time.localtime(create_time)
                    # 转换成新的时间格式()
                    create_time = time.strftime("%Y/%m/%d", time_local)
                    create_time_list.append(create_time)
                except KeyError:
                    create_time = response['data']['video']['created_time']
                    time_local = time.localtime(create_time)
                    # 转换成新的时间格式()
                    create_time = time.strftime("%Y/%m/%d", time_local)
                    create_time_list.append(create_time)
                except:
                    play_time_list.append('')


                #游戏时长
                play_time_list.append("")


                #帖子分区
                label = response['data']['moment']['groups'][0]['group_label']['name']
                label_list.append(label)
                #图片链接
                try:
                    img=response['data']['moment']['extended_entities']['images'][0]['url']
                    img_list.append(img)
                except KeyError:
                    img_list.append('')

                ### 标题
                try:
                    title = response['data']['moment']['sharing']['description']
                    title_list.append(title)
                except KeyError:
                    title=response['data']['moment']['extended_entities']['videos'][0]['title']
                    title_list.append(title)
                # 内容
                try:
                    content=response['data']['moment']['contents']['raw_text']
                    content_list.append(content)
                except KeyError:
                    content = response['data']['video']['intro']['text']
                    pattern = re.compile('[\u4e00-\u9fa5].*\Z')
                    content = re.search(pattern, content).group()
                    content=re.sub('</p>', '', content)
                    content_list.append(content)


                #回复
                reply_list.append("")

             # 休眠
            time.sleep(random.randrange(1, 2))
        # 保存为字典
        data_dict ={"name":name_list
                ,"createtime":create_time_list
                ,"label":label_list
                ,"playtime":play_time_list
                ,"title":title_list
                ,"content":content_list
                ,"img":img_list
                ,"reply":reply_list
                ,"user_url": self.list   }
        return data_dict
    #保存文件
    def save(self,name,dict):
        path = os.getcwd()
        filepath = open(path + '\%s.json' % name, 'w+', encoding='utf-8')
        json.dump(dict, filepath, ensure_ascii=False)
        excel_path=os.path.join(path,'%s.xlsx'%name)
        excel = pd.DataFrame(dict).to_excel(excel_path)


        print(path+'\%s.json' % name,excel_path)

    def run(self,name):
        data = self.parseplayer()
        json = self.save(name,dict=data)



if __name__ == "__main__":
    page = int(input('请输入页数：'))
    name = input('请输入保存文件的文件名称：')
    tapspider(42949,page).run(name)
    finish = input('按任意键退出程序')





























