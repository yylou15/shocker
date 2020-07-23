from csu.apis import *

global session
while True:
    print("0：退出，1: 查询用户基本信息，2：查询用户详细信息")
    command = input()
    if command == "0":
        exit(0)
    if command == "1":
        print(find_user(input("输入姓名：")))
    if command == "2":
        session = web_page_login(input("输入查询者user id："))
        session = sso_redirect_with_channel(session, "xsgzxt")
        print(session.cookies)
        print(session.post("http://202.197.71.125/a/workstudy/gXQZ0202/query_student", {
            "value": input("输入被查者学号：")
        }).text)