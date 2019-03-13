from urllib import request, error
import io
import sys

import codecs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
if __name__ == '__main__':
    url = "http://www.wtoip.com"

    # 使用代理步骤
    # 1. 设置代理地址
    proxy = {'http': '120.194.18.90:81'}
    # 2. 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3. 创建Opener
    opener = request.build_opener(proxy_handler)
    # 4. 安装Opener
    request.install_opener(opener)

    # 现在如果访问url，则使用代理服务器
    try:
        print('aaa')
        rsp = request.urlopen(url)
        html = rsp.read().decode('utf-8')
        print(html)
        with codecs.open('C:\\Users\\Administrator\\Desktop\\baidu.txt', 'w+', 'utf-8') as bai:
            bai.write(html)

    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
