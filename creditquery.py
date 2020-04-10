# coding:utf-8
from locust import HttpLocust,TaskSet,task
import json
class UserIndex(TaskSet):
    '''用户行为：打开我的博客首页demo'''
    @task(1)
    def open_blog(self):
        # 定义requests的请求头
        header = None
        r = self.client.post("/openApi/v1/creditquery",  headers=header, data=json.dumps({
    "merchantUserId":"10133099161597293",
    "merchantId":2020000802,
    "appId":2019010924,
    "timestamp":1577158821943,
    "version":"1.0",
    "sign":"YS3zxZvSoG52%)($"
}),verify=False)
        print(r.status_code)
        assert r.status_code == 200

class websitUser(HttpLocust):
    task_set = UserIndex
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f creditquery.py --host=https://api-test.nanopay.in.fg-example.com")