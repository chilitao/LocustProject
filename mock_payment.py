# coding=utf-8


import json
from flask import Flask, make_response
from time import sleep

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 指定返回体的内容
@app.route('/api_1', methods=['POST', 'GET'])
def api_1():
    status_code = 200
    result = {
        "code": 0,
        "msg": "success, api_1"
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


# 模糊匹配url,比如/api_2/foo/foo或/api_2
@app.route('/api_2', defaults={'path': ''},methods=['GET', 'POST'])
@app.route('/api_2/<path:path>', methods=['GET', 'POST'])
def api_2(path):
    status_code = 200
    result = {
        "code": 2,
        "msg": "some error massage,api_2"
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


# 响应超时
@app.route('/api_3', methods=['POST', 'GET'])
def api_3():
    sleep(5)
    status_code = 200
    result = {
        "code": 3,
        "msg": "you will wait or never get this smg, api_3"
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


# 指定httpcode=502
# 模糊匹配url,比如/api_4/foo/foo或/api_2
@app.route('/api_4', defaults={'path': ''},methods=['GET', 'POST'])
@app.route('/api_4/<path:path>', methods=['GET', 'POST'])
def api_4(path):
    status_code = 502
    result = """
            <html>
            <head><title>502 Bad Gateway</title></head>
            <body bgcolor='white'>
            <center><h1>502 Bad Gateway</h1></center>
            <hr><center>nginx/1.4.6 (Ubuntu)</center>
            </body>
            </html>
            """
    response = make_response(result, status_code)
    # response.headers["Content-Type"] = "application/json"
    return response


# 指定httpcode=401
# 模糊匹配url,比如/api_4/foo/foo或/api_2
@app.route('/api_5', defaults={'path': ''},methods=['GET', 'POST'])
@app.route('/api_5/<path:path>', methods=['GET', 'POST'])
def api_5(path):
    status_code = 401
    result = "401 Unauthorized"
    response = make_response(result, status_code)
    # response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    # app.run()参数不要修改
    # app.run()参数不要修改
    # app.run()参数不要修改
    app.run(host = '127.0.0.1', debug = False, port = 5001)
