from urllib import parse, request
from http import cookiejar
'''
sdasdsadsadsadsad
打撒打撒多撒多
'''

filename = 'cookie1.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)


def login(email, password):
    data = {
        'email': email,
        'password': password
    }
    headers = {
        'Content-Length': len(data)
    }
    data = parse.urlencode(data)
    req = request.Request('http://www.renren.com/PLogin.do', data=data.encode())
    rsp = opener.open(req)
    cookie.save(ignore_expires=True, ignore_discard=True)


def getHome():
    cookie.load('cookie1.txt', ignore_discard=True, ignore_expires=True)
    req = request.Request('http://page.renren.com/')
    rsp = opener.open(req)
    print(rsp.read().decode())


if __name__ == '__main__':
    getHome()
