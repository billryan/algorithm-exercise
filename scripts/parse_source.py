#!/usr/bin/env python

from pyquery import PyQuery as pq


class Lintcode(object):
    def __init__(self):
        self.url_algo = "http://www.lintcode.com/en/problem/"

    def get_src_page(src_url):
        src_page = pq(url=src_url)
        return src_page

    def get_src_detail(src_page):
        problem_detail = src_page('#problem-detail')
        difficulty_level = problem_detail('h4')('.label').text()
        title = problem_detail('h4')('.m-l-sm').text()
        raw_tags = problem_detail('#tags')('a')
        tags = [tag.text for tag in raw_tags]
        raw_detail = src_page('#problem-detail')('div')


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
