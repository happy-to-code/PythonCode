import requests
from lxml import html

# 需要爬数据的网址
url = 'https://movie.douban.com/'
page = requests.Session().get(url)
tree = html.fromstring(page.text)
# 获取需要的数据
result = tree.xpath('//td[@class="title"]//a/text()')
print(result)
