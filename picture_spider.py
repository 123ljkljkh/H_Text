# 致美化网页电脑壁纸爬取.py

from time import sleep
import requests
import bs4
from bs4 import BeautifulSoup
import re



def getHTMLDate(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillDate(html, name_list, url_list):
    counts = 0
    soup = BeautifulSoup(html, 'html.parser')
    for td in soup.find('div', class_="slist").find_all('li'):
        if isinstance(td, bs4.element.Tag):
            date = td.find('img').attrs
            name_list.append(date['alt'])
            url_list.append(date['src'])

    # picture_url="http://pic.netbian.com/uploads/allimg/220802/231950-1659453590cc8e.jpg"
    # print(len(soup.find('div',class_="slist").find_all('li')))


def getPicDate(name_list, url_list):
    global picture_counts
    basic_url = "http://pic.netbian.com"
    file_path = "C:\\Users\\Administrator\\Pictures\\Camera Roll\\picspider\\"
    for i in range(len(name_list)):
        url = basic_url+url_list[i]
        name = name_list[i]
        pic = requests.get(url)
        with open(file_path+'{}.jpg'.format(name), 'ab') as f:
            picture_counts += 1
            f.write(pic.content)
            f.close()
            print(picture_counts, '  ->  '+name+'  ->  '+"文件保存成功")
            sleep(0.5)


def main():
    start_page = 15
    end_pages = 30
    basic_url = "http://pic.netbian.com/"
    for i in range(start_page, end_pages+1):
        name_list = []
        url_list = []
        if i == 1:
            end_url = "index.html"
            url = basic_url+end_url
            html = getHTMLDate(url)
            fillDate(html, name_list, url_list)
            getPicDate(name_list, url_list)
        else:
            end_url = "index_{}.html".format(i)
            url = basic_url+end_url
            html = getHTMLDate(url)
            fillDate(html, name_list, url_list)
            getPicDate(name_list, url_list)
        sleep(3)


picture_counts = 0
main()


# "http://pic.netbian.com/index.html"
# "http://pic.netbian.com/index_2.html"
