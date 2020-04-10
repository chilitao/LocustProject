import requests as R
import json
from randomdigit import *
url="http://api-test.nanopay.in.fg-example.com/openApi/v1/ordercreate"
header = {'Content-Type': 'application/json'}
thirdOrderId=rand_num(12)
merchantUserId=rand_num(18)
data={
    "merchantId":2020000808,
    "thirdOrderId":thirdOrderId,
    "orderAmount":"200",
    "transType":7,
    "expireTime":888888,
    "merchantUserId":"32033708",
    "installmentId":1,
    "goodsName":[
        {
            "goodsName":"big apples"
        }
    ],
    "appId":2019010925,
    "timestamp":1582547787122,
    "version":"1.0",
    "sign":"YS3zxZvSoG52%)($"
}
res=R.post(url=url,headers=header,data=json.dumps(data)).json()

ts=res['data']['transSerial']
tc=res['data']['tmpCode']

url1="https://h5.nanopay.in.fg-example.com/h5sdk/home/index.html?tmpCode=%s&transSerial=%s"%(tc,ts)
print(url1)