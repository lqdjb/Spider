'''\
URLError的使用
'''

from urllib import request, error


if __name__ == '__main__':

    # url = "http:iiiiiiiiidu//www.baidu.com/welcome.html"

    url = "http://www.baidu.com"
    try:

        req = request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        rsp = request.urlopen( req )
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)