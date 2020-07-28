from csu.apis import *

global session
while True:
    print("-------")
    print("0：退出，1: 查询用户基本信息，2：登录，3：查询用户信息（需登录），4：扫码登录")
    command = input()
    if command == "0":
        exit(0)

    if command == "1":
        for user in find_user(input("输入姓名：")):
            print(user)

    if command == "2":
        session = web_page_login(input("输入查询者user id："))
        session = sso_redirect_with_channel(session, "xsgzxt")
        for cookie in session.cookies:
            print(cookie)

    if command == "3":
        print(session.post("http://202.197.71.125/a/workstudy/gXQZ0202/query_student", {
            "value": input("输入被查者学号：")
        }).text)

    if command == "4":
        scan_qr_code_login(input("输入token id："), input("输入user id："))
