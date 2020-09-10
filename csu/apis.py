import json
import re

import requests

from csu.gateway import req, baseRequestBody


def query_user_info(user_id):
    return req("queryUserInfo", {"query_user_id": str(user_id)})


def find_user(keyword):
    res = req("findUser", {"keyword": str(keyword)})
    for user in res['data']['users']:
        yield [user['userId'], user['userName'], user['type'], user['dept']]


def portal_login(token_id, user_id):
    baseRequestBody["head"]["user_id"] = str(user_id)
    return req("portalLogin", {"tokenId": str(token_id)})


def web_page_login(user_id):
    web_sess = requests.Session()
    web_sess.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    web_sess.get("http://my.csu.edu.cn/login/index.jsp")
    token_id = json.loads(web_sess.post("http://my.csu.edu.cn/cgi-bin/login", {
        "method": "getQrCode"
    }).text)["tokenId"]
    portal_login(token_id, user_id)
    web_sess.post("http://my.csu.edu.cn/cgi-bin/login", data={
        "method": "qrCodeLogin",
        "tokenId": token_id
    })
    return web_sess


def sso_redirect_with_channel(session, channel_name):
    form_html = session.post(
        "http://my.csu.edu.cn/portal/ssoRedirect.jsp?channelName=" + channel_name + "&continueURL=").text
    action = re.search(r'action="(.*)"', form_html).group(1)
    inputs = re.findall(r'input\sname="(.*?)" type="hidden" value="(.*?)"', form_html)
    data = {}
    for input_ in inputs:
        data[input_[0]] = input_[1]
    res = session.post(action, data)
    return session


def scan_qr_code_login(token_id, user_id):
    return portal_login(token_id, user_id)
