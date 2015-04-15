#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crawling data from web
"""
import requests
import sys
from bs4 import BeautifulSoup

TANG_URL = 'http://so.gushiwen.org/gushi/tangshi.aspx'
TANG_FILE = './data/tang'


class Poem(object):
    """class to get poem"""
    def __init__(self, home_url, filename):
        """init"""
        self._home_url = home_url
        self._bash_url = 'http://' + home_url.split('/')[2]
        self._file = filename

    def _get_url(self, url):
        """get content in url, return text"""
        r = requests.get(url)
        return r.text.encode(r.encoding)

    def get_home(self):
        """get the home page"""
        # get the home page
        html = self._get_url(self._home_url)
        # print html

        # get the sub poem url
        soup = BeautifulSoup(html)
        pages = soup.select('span a')
        urls = []
        for page in pages:
            url = page.attrs['href']
            urls.append(self._bash_url+url)

        fd = open(self._file, 'w')
        for url in urls:
            data = self.get_page(url)
            title = u'[32m《' + data['title'] + u'》[m' + '\n'
            fd.write(title.encode('utf8'))
            author = u'[33m' + data['author'] + u'[m' + '\n'
            fd.write(author.encode('utf8'))
            body = data['body'].replace(u'！', u'。')
            body = body.replace(u'？', u'。')
            body = body.split(u'。')
            body = '\n'.join(body)
            fd.write(body.encode('utf8'))
            fd.write('\n%\n')
        fd.close()

    def get_page(self, url):
        """get poem page"""
        print 'get: %s' % url
        html = self._get_url(url)
        # print html

        soup = BeautifulSoup(html)
        main_body = soup.find('div', class_='main3')
        poem_tag = main_body.find('div', class_='son2')
        poem = poem_tag.text
        poem_info = poem.split()
        author = poem_info[3]
        body = poem_info[5:]
        title = soup.h1.get_text()
        data = {}
        data['title'] = title
        data['author'] = author
        data['body'] = ''.join(body)
        print title + '-'*10,
        if len(body) > 0:
            print 'ok'
        else:
            print 'error'
        return data


if __name__ == '__main__':
    argc = len(sys.argv)
    url = TANG_URL
    filename = TANG_FILE
    if argc > 1:
        url = sys.argv[1]
    if argc > 2:
        filename = sys.argv[2]
    p = Poem(url, filename)
    p.get_home()
