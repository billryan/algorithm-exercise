#!/usr/bin/env python

import os
import sys
from pyquery import PyQuery as pq
import html2text


class Lintcode(object):
    def __init__(self):
        self.url_algo = "http://www.lintcode.com/en/problem/"

    def get_src_page(self, src_url):
        src_page = pq(url=src_url)
        return src_page

    def get_src_detail(self, src_url):
        src_page = self.get_src_page(src_url)
        src_detail = {}
        problem_detail = src_page('#problem-detail')
        difficulty_level = problem_detail('h4')('.label').text()
        title = problem_detail('h4')('.m-l-sm').text()
        raw_tags = problem_detail('#tags')('a')
        tags = [tag.text for tag in raw_tags]
        raw_detail = src_page('#problem-detail')('div').html()
        body_start = raw_detail.find('<p>')
        body_end = raw_detail.find('<b>Tags</b>')
        raw_body = raw_detail[body_start:body_end]
        body = raw_body.replace('<b>', '<h4>')
        body = body.replace('</b>', '</h4>')
        src_detail['title'] = title
        src_detail['tags'] = tags
        src_detail['level'] = difficulty_level
        src_detail['body'] = body
        return src_detail


class Leetcode(object):
    def __init__(self):
        self.url_algo = "https://leetcode.com/problemset/algorithms/"

    def get_src_page(src_url):
        return pq(url=src_url)

    def get_src_tags(src_page):
        raw_tags = src_page('.btn.btn-xs.btn-primary')
        return [tag.text() for tag in raw_tags.items()]

    def get_src_title(src_page):
        raw_title = src_page('title').text().split('|')[0][:-1]

    def get_difficulty(src_page):
        search_url = "https://leetcode.com/problemset/algorithms/"


def main(argv):
    if (len(argv) != 2):
        print("Usage: python parse_source.py problem_url")
    scripts, url = argv
    lintcode = Lintcode()
    src_body = lintcode.get_src_detail(url)['body']
    h = html2text.HTML2Text()
    print(h.handle(src_body))

if __name__ == "__main__":
    main(sys.argv)
