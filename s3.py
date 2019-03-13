import codecs
if __name__ == '__main__':
    with codecs.open('C:\\Users\\Administrator\\Desktop\\baidu.txt', 'a','utf-8') as bai:
        bai.write('ccc')
    with codecs.open('C:\\Users\\Administrator\\Desktop\\baidu.txt', 'r+','utf-8') as bai:
        print(bai.read())
