import json

import requests

from des import encrypt, decrypt

gatewayUrl = "http://app.its.csu.edu.cn:80/mqtt/execute.jsp"
session = requests.Session()
head = {
    "Host": "app.its.csu.edu.cn:80",
    "User-Agent": "android-async-http/1.4.1 (http://loopj.com/android-async-http)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

baseRequestBody = {
    "head": {"command_id": "", "user_password": "", "request_tick": "", "terminal_name": "Android",
             "app_version": "2.19", "osVersion": "8.0.0", "user_id": "3850459", "osName": "HUAWEI 999",
             "app_id": "zhongnanim", "uuid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
             "terminal_id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"},
    "data": {}

}


def req(command_id, data):
    baseRequestBody["head"]["command_id"] = command_id
    baseRequestBody["data"] = data
    res = session.post(url=gatewayUrl, data={
        "string": encrypt(json.dumps(baseRequestBody)).decode(),
        "app_version": "2.19"
    }).text.strip().replace(" ", "")
    return json.loads(decrypt(res).decode())


