import requests
from csu.apis import sso_redirect_with_channel

session = requests.Session()
session = sso_redirect_with_channel(session, "zndxjyzdzx")
print(session.get("http://career.csu.edu.cn/home/index").text)
