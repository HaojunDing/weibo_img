from fengzhuang import urlrequest
import json
import os
from urllib import request

def cards(url,page):

    html = urlrequest(url%page).decode('utf-8')
    json_dict = json.loads(html)
    data = json_dict['data']['cards']
    return data

def pics(data):
    try:
        for i in data:
            pic = i['mblog']['pics']
            for j in pic:
                # print(j['large']['url'])
                try:
                    download(j['large']['url'])
                except:
                    print('无法下载%s'%j)
    except KeyError as e :
        print(e)


a = 0


def download(img_url):
    # print(type(img_url),'传进去的值')
    global a
    a += 1
    request.urlretrieve(img_url,'./faye/'+str(a)+'.jpg')
    print('下载到第%d张图片' % a)


if __name__ == '__main__':
    b = 0
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6098222807&containerid=1076036098222807&page=%d'
    start_page = int(input('请输入从第几页开始爬取:'))
    page = int(input('请输入爬取到第多少页:'))
    for i in range(start_page,page+1):
        data = cards(url, page=i)
        pic = pics(data)
