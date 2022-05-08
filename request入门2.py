import requests

url = "https://fanyi.baidu.com/sug"

word = input("请输入你要翻译的单词")
my_data = {"kw": word}
head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
}
resp = requests.post(url, data=my_data,headers=head)

print(resp.json())
resp.close()