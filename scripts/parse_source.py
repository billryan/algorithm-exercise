#!/usr/bin/env python3
"""Parse Leetcode/Lintcode html page to markdown."""

import sys
from pyquery import PyQuery
import requests
import html2text


class Code(object):
    """Leetcode/Lintcode base."""

    def __init__(self, arg):
        """Init."""
        super(Code, self).__init__()
        self.arg = arg
        self.raw_p_html = None

    def get_raw_p_html(self, url):
        """Get raw problem html page."""
        self.raw_p_html = PyQuery(url=url)
        return self.raw_p_html

    def get_p_body(self, raw_p_html):
        """Get problem html body only."""
        pass

    def get_p_title(self, raw_p_html):
        p_title = raw_p_html('title').text().split('|')[0].strip()
        return p_title

    def get_p_tags(self, raw_p_html):
        pass

    def get_p_difficulty(self, raw_p_html):
        pass


class Lintcode(Code):

    def __init__(self):
        super(Lintcode, self).__init__()

    def get_src_detail(self, src_url):
        src_page = self.get_src_page(src_url)
        src_detail = {}
        problem_detail = src_page('#problem-aside')
        # difficulty_level = problem_detail('h4')('.label').text()
        title = problem_detail('h4')('a').text().strip()
        raw_tags = problem_detail('#tags')('a')
        tags = [tag.text for tag in raw_tags]
        raw_detail = src_page('#problem-aside')('#description').html()
        body_start = raw_detail.find('<p>')
        body_end = raw_detail.find('<b>Tags</b>')
        raw_body = raw_detail[body_start:body_end]
        body = raw_body.replace('<b>', '<h4>')
        body = body.replace('</b>', '</h4>')
        src_detail['title'] = title
        src_detail['tags'] = tags
        # src_detail['level'] = difficulty_level
        src_detail['body'] = body
        return src_detail


class Leetcode(Code):

    def __init__(self, arg):
        super(Leetcode, self).__init__(arg)

    def get_p_body(self, raw_p_html):
        """Get the main content of problem."""
        q_content_html = raw_p_html('.question-content').html()
        p_body_start = q_content_html.find('<p>')
        p_body_end = q_content_html.find('<div>')
        p_body = q_content_html[p_body_start:p_body_end]
        # body = p_body.replace('<b>', '<h4>')
        # body = body.replace('</b>', '</h4>')
        return p_body

    def get_p_tags(self, raw_p_html):
        p_tags = []
        try:
            raw_tags = raw_p_html('.btn.btn-xs.btn-primary')
            for tag in raw_tags:
                if tag.attrib['href'].startswith('/tag/'):
                    p_tags.append(tag.text)
        except Exception as err:
            print('Error: ', err)
        return p_tags

    def get_p_difficulty(self, raw_p_html):
        return raw_p_html('.question-info.text-info').text().split(' ')[-1]


def main(argv):
    if (len(argv) != 2):
        print("Usage: python parse_source.py problem_url")
    scripts, url = argv
    url = url.strip().rstrip('/').replace('/zh-cn/', '/en/')
    p_url_name = url.split('/')[-1]

    lintcode_site = 'http://www.lintcode.com/en/problem/'
    leetcode_site = 'https://leetcode.com/problems/'
    p_urls = {}
    p_html_inst = Code(url)
    h = html2text.HTML2Text()
    if url.startswith(lintcode_site):
        p_urls['lintcode'] = url
        leetcode_url = leetcode_site + p_url_name + '/'
        response = requests.head(leetcode_url)
        if response.status_code == 200:
            p_urls['leetcode'] = leetcode_url
        p_html_inst = Lintcode(url)
    elif url.startswith(leetcode_site):
        p_urls['leetcode'] = url + '/'
        lintcode_url = lintcode_site + p_url_name + '/'
        response = requests.head(lintcode_url)
        if response.status_code == 200:
            p_urls['lintcode'] = lintcode_url
        p_html_inst = Leetcode(url)
    else:
        pass
    raw_p_html = p_html_inst.get_raw_p_html(url)
    p_title = p_html_inst.get_p_title(raw_p_html)
    p_body = p_html_inst.get_p_body(raw_p_html)
    p_difficulty = p_html_inst.get_p_difficulty(raw_p_html)
    raw_p_tags = p_html_inst.get_p_tags(raw_p_html)
    raw_p_tags.append(p_difficulty)
    lines = []
    lines.append('# ' + p_title + '\n')
    p_tags = ['TAG_' + tag for tag in raw_p_tags]
    tags = ' '.join(p_tags)
    lines.append('**TAGS:** ' + tags + '\n')
    lines.append('## Question' + '\n')
    # generate leetcode/lintcode source url lists
    for key in sorted(p_urls):
        p_list = '- ' + key + ': ' + '[' + p_title + '](' + p_urls[key] + ')'
        lines.append(p_list)
    lines.append('\n### Problem Statement\n')
    lines.append(h.handle(p_body))
    print('\n'.join(lines))

if __name__ == "__main__":
    main(sys.argv)
