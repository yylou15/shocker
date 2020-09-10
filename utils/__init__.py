import re

import requests

from csu.apis import find_user


def select_user():
    users = list(find_user(input("输入姓名：")))
    idx = 0
    if len(users) > 1:
        for user in users:
            print(str(idx) + str(user))
            idx += 1
        idx = input("哪个？")
        return users[int(idx)][0]
    elif len(users) == 1:
        return str(users[0][0])
    else:
        return None


def get_sys_name_from_login_url(url):
    session = requests.Session()
    res = session.post(url, data={
        "userName": 3901170504,
        "passWord": 158718,
        "enter": "true"
    })

    return re.search(r'<input\sname="Thirdsys"\stype="hidden"\svalue="(.*?)"', res.text).group(1)


if __name__ == '__main__':
    print(get_sys_name_from_login_url("http://ca.its.csu.edu.cn/home/login/75"))
