import time
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup

baseurl = 'https://umei.cc/meinvtupian/'
urls = {"1": 'xingganmeinv/', "2": 'siwameinv/', "3": "meinvxiezhen/", "4": "waiguomeinv/", "5": "nayimeinv/", }
select_url = input('''
请输入你要抓取的风格序号
1:普通级
2:清晰级
3:写真级
4:国际级
5:时尚级
''')
url = f"https://umei.cc/meinvtupian/{urls[select_url]}"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
page = BeautifulSoup(resp.text, 'html.parser')
pic_boxs = page.find("ul", attrs={"class": "pic-list after"})
pic_box = pic_boxs.findAll("li")
pic_hrefs = []
for pic_li in pic_box:
    # print(pic_li)
    href = pic_li.find('a')
    src = href.get("href")
    # print(src)
    pic_hrefs.append("https://umei.cc" + src)

print(pic_hrefs)
length = len(pic_hrefs)
img_file = Path("./image")
if not img_file.is_dir():
    print("不存在文件夹,正在创建image文件夹..")
    os.mkdir("image")

print(f"总计{length}张图片")
x = 0
for href in pic_hrefs:
    x += 1
    new_page = requests.get(href)
    new_page.encoding = "utf-8"
    img_page = BeautifulSoup(new_page.text, "html.parser")
    img_box = img_page.find("section", attrs={"class": "img-content"})
    img = img_box.find("img")
    src = img.get('src')
    img_file = requests.get(src)
    img_name = src.split('/')[-1]
    with open("image/" + img_name, mode="wb") as f:
        f.write(img_file.content)

    print(f'{img_name} 抓取完成{x}/{length}')
    time.sleep(0.1)

print('全部抓取完成')
