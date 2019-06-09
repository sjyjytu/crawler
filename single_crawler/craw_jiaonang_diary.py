import requests
import codecs
import json
from requests.exceptions import RequestException
import re
import time
# import multiprocessing


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response = response.text
            return response
        else:
            return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<div class="diary">.*?<div class="body">.*?<div class="title">.*?<a class="name"'
                         + '.*?>(.*?)</.*?<p class="content">[\s]*(<a.*</a>)?(.*?)[\s]*</p>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "name": item[0],
            "content": item[2],
        }


def write_to_file(content, file_num):
    with codecs.open('result%d'%file_num, 'a', 'utf-8') as f:
        # f=codecs.open('result.txt','a','utf-8')
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset, file_num):
    url = 'http://www.timepill.net/' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item, file_num)


# print html

# if __name__ == '__main__':
#     pool = multiprocessing.Pool()
#     pool.map(main, [i * 20 for i in range(10)])
iter_num = 0
num_per_hour = 3
while True:
    file_num = iter_num//(24*num_per_hour)
    iter_num += 1
    for i in range(40):
        main(i*20, file_num)
    print('iter num:%d'%iter_num)
    time.sleep(60*30//num_per_hour)
