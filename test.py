from csu.apis import portal_login, web_page_login

print(web_page_login(40581046).post("http://my.csu.edu.cn/cgi-bin/app", data={
        "method": "queryAllCsuApps"
    }).text)