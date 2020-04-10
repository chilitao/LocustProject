import requests as R
import json
from randomdigit import *
from mysql import sql
url="http://api-test.nanopay.in.fg-example.com/openApi/v1/ordercreate"
header = {'Content-Type': 'application/json'}
thirdOrderId=rand_num(12)
sqlmerchant="SELECT merchant_user_id FROM np_pre_credit WHERE pre_credit_amount>1900 AND active_status=0 AND batch_credit=1 AND np_user_id=0 AND merchant_id=2020000802 "
merchantUserId=sql(sqlmerchant)[0]
print(merchantUserId)

data={
    "merchantId":2020000802,
    "thirdOrderId":str(thirdOrderId),
    "orderAmount":"100",
    "transType":6,
    "expireTime":888888,
    "merchantUserId":merchantUserId,
    "installmentId":1,
    "goodsName":[
        {
            "goodsName":"banana"
        }
    ],
    "appId":2019010924,
    "timestamp":1582547787122,
    "version":"1.0",
    "sign":"YS3zxZvSoG52%)($"
}
res=R.post(url=url,headers=header,data=json.dumps(data)).json()

ts=res['data']['transSerial']
tc=res['data']['tmpCode']

url1="https://h5.nanopay.in.fg-example.com/h5sdk/home/index.html?tmpCode=%s&transSerial=%s"%(tc,ts)
print(url1)