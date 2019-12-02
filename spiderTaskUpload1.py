import hashlib
import requests
import json
from datetime import datetime
import time
import random

# todo 线索内容 修改此处（销售需要与下面的门店对应）
upload_data = [
    {
        'customerName': '张三',
        'customerPhone': str(str(random.randint(130, 139)) + str(random.randint(10000000, 99999999))),
        'intentCarModel': None,
        'registerDateTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'extData': {},
        'spiderCrawlLogId': 1,
        'salesName': 'f',
        'sourceCategory': 'DCC-400==>400-汽车之家'
    },
    {
        'customerName': '李四',
        'customerPhone': str(str(random.randint(130, 139)) + str(random.randint(10000000, 99999999))),
        'intentCarModel': None,
        'registerDateTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'extData': {},
        'spiderCrawlLogId': 1,
        # 'salesName': None,
        'salesName': 'f',
        'sourceCategory': 'DCC-400==>400-汽车之家'
    }

    # {
    #     'customerName': '李四',
    #     'customerPhone': str(str(random.randint(130, 139)) + str(random.randint(10000000, 99999999))),
    #     'intentCarModel': None,
    #     'registerDateTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #     'extData': {},
    #     'spiderCrawlLogId': 1,
    #     'salesName': 'Linda Li',
    #     'sourceCategory': 'DCC-400==>400-保时捷'
    # }

    # {
    #     "customerName": "客户",
    #     "customerPhone": "15366965183",
    #     "intentCarModel": "空",
    #     "registerDateTime": "2019-11-13 12:23:33",
    #     "extData": {},
    #     "spiderCrawlLogId": 128744,
    #     "salesName": "f",
    #     "sourceCategory": "DCC-400==＞400-汽车之家"
    # },
    # {
    #     "customerName": "客户",
    #     "customerPhone": "15366965183",
    #     "intentCarModel": "空",
    #     "registerDateTime": "2019-11-13 12:20:44",
    #     "extData": {},
    #     "spiderCrawlLogId": 128744,
    #     "salesName": "f",
    #     "sourceCategory": "DCC-400==＞400-汽车之家"
    # }

    # {
    #     "customerName": "李四",
    #     "customerPhone": "13512637350",
    #     "intentCarModel": None,
    #     "registerDateTime": "2019-11-20 16:38:21",
    #     "extData": {},
    #     "spiderCrawlLogId": 1,
    #     "salesName": None,
    #     "sourceCategory": "DCC-400==＞400-易车"
    # },
    # {
    #     "customerName": "李四",
    #     "customerPhone": "13569438926",
    #     "intentCarModel": None,
    #     "registerDateTime": "2019-11-20 16:38:21",
    #     "extData": {},
    #     "spiderCrawlLogId": 1,
    #     "salesName": None,
    #     "sourceCategory": "DCC-400==＞400-易车"
    # }

]

# todo 来源/门店（需要与上面的销售对应）
upload_body = dict()
upload_body['data'] = json.dumps(upload_data, ensure_ascii=False)
upload_body['orgId'] = 29
upload_body['followDate'] = '2019-11-05 10:06:00'
upload_body['followBy'] = 'CcUser'

# 排序
upload_body_keys = upload_body.keys()
upload_body_keys = sorted(upload_body_keys)
# 拼接加密参数
encrypt_params = ''
for key in upload_body_keys:
    encrypt_params += str(upload_body[key])
# 参数加密
upload_body['signatureKey'] = hashlib.sha256(
    (encrypt_params + 'YXdkaXVhd2ZoaTI4OTc0MjYzOHJzZCYjMzk7W3ANCl0=').encode('utf-8')).hexdigest()

print('请求内容：%s' % upload_body)
response = requests.post('http://localhost:8081/business/client/presaleData/pyUpload', data=upload_body)
print('响应内容：%s' % response.text)
