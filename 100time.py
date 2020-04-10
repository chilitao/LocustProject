import requests as R
import json
from randomdigit import *
goods=["苹果",'香蕉',"香梨","橘子"]
def run():
    url = "http://localhost:8000/product/api/"
    header = {'Content-Type': 'application/json'}
    for i in range(len(goods)):
        price = rand_num(2)
        data = {
            "name": goods[i],
            "price": price}
    res = R.post(url=url, headers=header, data=json.dumps(data)).json()

    print(res)

if __name__=='__main__':
    for i in range(4):
        run()
