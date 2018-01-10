#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import markdown


CSDN_PUBLISH_URL = 'http://mp.blog.csdn.net/mdeditor/setArticle'


def post_data(submiturl, title, markdownpath, tags, categories, channel,private='0'):
    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7,en-GB;q=0.6',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Host': 'mp.blog.csdn.net',
               'Cookie': '',
               'Origin': 'http://mp.blog.csdn.net',
               'Referer': 'http://mp.blog.csdn.net/mdeditor',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'

    }
    markdowncontent = ''
    with open(markdownpath, 'r', encoding='utf-8') as f:
        markdowncontent = f.read()


    html_content = markdown.markdown(markdowncontent)

    formdata = {
        'title': title,
        'markdowncontent': markdowncontent,
        'content': html_content,
        'id': '',
        'private': private,
        'tags': tags,
        'status': 0,
        'categories': categories,
        'channel': channel,
        'type': 'original',
        'articleedittype': '1'
    }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    req = urllib.request.Request(submiturl, data, headers, method='POST')

    response = urllib.request.urlopen(req)

    print("csdn send result : %s, %s" % (response.status, response.reason))


#md trans to html
def parse_to_html(markdown):
    return ''


url = CSDN_PUBLISH_URL
post_data(url, 'testtitle123456', 'E:/quick_use.md', '标记1', 'categories1', 12, '0')
