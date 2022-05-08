import requests
from bs4 import BeautifulSoup

url = 'https://music.douban.com/chart'
head = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
resp = requests.get(url, headers=head)
# print(resp.text)
page = BeautifulSoup(resp.text, 'html.parser')
# print(page)
res = page.find("ul", attrs={
    "class": "col5"
})

music = res.find_all("div", attrs={
    "class": "intro"
})
for i in music:
    ires = i.find("p")
    print(ires.text)
# print(mres)
