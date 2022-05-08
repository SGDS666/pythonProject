# 拿到页面源代码
# 通过re获取有效信息
import requests
import re

url = "https://movie.douban.com/top250"
head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
resp = requests.get(url, headers=head)
content = resp.text
# print(content)
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
result = obj.finditer(content)
for i in result:
    print(i.group("name"))
resp.close()
