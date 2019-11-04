# 导入requests包
import requests

url = 'http://www.cntour.cn/'
# Get方式获取网页数据
strhtml = requests.get(url)
print(strhtml.text)
