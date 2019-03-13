from urllib import request, parse
from http import cookiejar

filename = 'cookie2.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
url = 'http://fanyi.youdao.com'
req = request.Request(url)
opener.open(req)
cookie.save(ignore_expires=True, ignore_discard=True)


def youdao(key):
    Requrl = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15524435095795',
        'sign': 'a6441a4c64714a055aed4dbcf0f71196',
        'ts': '1552443509579',
        'bv': 'e3c02aca4dd13bbb3f44d334e1eb3d08',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }

    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": cookie.load(filename, ignore_discard=True, ignore_expires=True),
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    req = request.Request(url=Requrl, data=data, headers=headers)
    print(type(req))
    rsp = opener.open(req)
    print(rsp.read().decode())


if __name__ == '__main__':
    youdao('abandon')
