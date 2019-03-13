from urllib import request, parse
from http import cookiejar

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
url = 'https://www.wtoip.com'
rsp = request.Request(url)
response = opener.open(rsp)
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
print(response.read().decode())
