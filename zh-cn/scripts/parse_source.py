#!/usr/bin/env python

from pyquery import PyQuery as pq

def get_lc_src_tags(lc_page):
    raw_tags = lc_page('.btn.btn-xs.btn-primary')
    return [tag.text() for tag in raw_tags.items()]

def get_lc_src_title(lc_page):
    raw_title = lc_page('title').text().split('|')[0][:-1]

def get_lc_difficulty(lc_title):
    search_url = "https://leetcode.com/problemset/algorithms/"

def get_source_page(source_url):
    return pq(url=source_url)
