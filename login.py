import requests
from get_login_token import get_login_token
from initialize import initialize

def make_data(login_token,id,password):
    return f'''-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="__RequestVerificationToken"

{login_token}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="UserId"

{str(id)}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="Password"

{str(password)}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="UserType"

학생
-----------------------------325333128821718686562724141506--
'''

def login(s,login_token,id,password):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'multipart/form-data; boundary=---------------------------325333128821718686562724141506',
        'Origin': 'https://ksa.hs.kr',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://ksa.hs.kr/Account/Login',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = s.post('https://ksa.hs.kr/Account/Login', data = make_data(login_token,id,password).encode("utf-8"), headers=headers)

    # print(response.cookies)

    # print(response.text)
