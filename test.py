from csu.apis import *
import bs4

global session
while True:
    print("-------")
    print("0：退出，1: 查询用户基本信息，2：登录，3：查询用户信息（需登录），4：扫码登录，5：就业信息, 6: 就业信息plus")
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
        user_id = input("输入user id：")
        token_id = input("输入token id：")
        scan_qr_code_login(token_id, user_id)

    if command == "5":
        session = web_page_login(input("输入查询者user id："))
        session = sso_redirect_with_channel(session, "zndxjyzdzx")
        for cookie in session.cookies:
            print(cookie)

    if command == "6":
        users = list(find_user(input("输入姓名：")))
        idx = 0
        for user in users:
            print(user)

        if len(users) > 1:
            idx = input("哪个？")
            session = web_page_login(users[int(idx)][0])
        else:
            session = web_page_login(str(users[0][0]))

        session = sso_redirect_with_channel(session, "zndxjyzdzx")
        page = session.get("http://career.csu.edu.cn/melectronic/mstudent/online").text
        jiuye = re.search(r'href="(/melectronic/mstudent/viewInvitation/id/\d+)"', page)
        if jiuye:
            jiuyePage = bs4.BeautifulSoup(session.get("http://career.csu.edu.cn/" + jiuye.group(1)).text,
                                          features="html.parser")
            text1 = jiuyePage.find(class_="dl-list")
            text2 = jiuyePage.find_all(class_="text-right")[1]
            print(text1.getText())
            print(text2.getText())

        page = bs4.BeautifulSoup(session.get("http://career.csu.edu.cn/melectronic/mstudent/otherWay").text,
                                 features="html.parser")
        print(page.find("tbody").getText().strip())
