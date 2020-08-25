import requests
import re

sso_num = 0
while True:
    sso_num += 1
    url = "http://ca.its.csu.edu.cn/home/login/" + str(sso_num)
    res = requests.get(url).text
    caption = re.search(r'<span\sclass="style22"><em>(.*?)</em></span>', res)
    if caption and caption.group(1) != "用户登录":
        print(url, caption.group(1))
