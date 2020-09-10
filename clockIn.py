import json
import re
import sys

from csu.apis import sso_redirect_with_channel, web_page_login
from utils import select_user, get_sys_name_from_login_url

session = web_page_login(select_user(sys.argv[1]))
session = sso_redirect_with_channel(session, get_sys_name_from_login_url("http://ca.its.csu.edu.cn/Home/Login/215"))

main_page = session.get("https://wxxy.csu.edu.cn/ncov/wap/default/index?from=history").text
info = json.loads(re.search(r'var\sdef\s=(.*);', main_page).group(1).strip())
address_info = json.loads(info['geo_api_info'])['addressComponent']
info['szgj'] = address_info['country']
info['szcs'] = address_info['city']
info['szgjcs'] = "{} {}".format(address_info['country'], address_info['city'])
info['area'] = "{} {} {}".format(address_info['province'], address_info['city'], address_info['district'])

res = json.loads(session.post("https://wxxy.csu.edu.cn/ncov/wap/default/save", data=info).text)
print("打卡结果：{}，上次打卡地点：{}".format(res['m'], json.loads(info['geo_api_info'])['formattedAddress']))
