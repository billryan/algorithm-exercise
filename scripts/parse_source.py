#!/usr/bin/env python3
"""Parse Leetcode/Lintcode html page to markdown."""

import sys
from pyquery import PyQuery
import requests
import html2text


class OJHtml2Markdown(object):
    """Parse Leetcode/Lintcode html page to markdown."""

    def __init__(self, url, prefer_leetcode=False):
        """Init."""
        self._prefer_leetcode = prefer_leetcode
        url = url.strip().rstrip('/').replace('/zh-cn/', '/en/')
        key_end = url.find('.com/')
        self._site = url[key_end - 8:key_end]
        self._url = url
        self._raw_p_html = PyQuery(url=url)
        self._p_url_path = url.split('/')[-1]
        self._p_urls = {}

    def _lint2leet(self):
        """Replace lintcode with leetcode if prefer leetcode."""
        if self._url.startswith('https://leetcode.com/problems/'):
            return
        url = 'https://leetcode.com/problems/{}/'.format(self._p_url_path)
        response = requests.head(url)
        if response.status_code == 200:
            self._site = 'leetcode'
            self._url = url
            self._raw_p_html = PyQuery(url=self._url)

    def _gen_p_url_lists(self):
        """Generate leetcode/lintcode problem url lists."""
        leetcode_url = 'https://leetcode.com/problems/{}/'.format(self._p_url_path)
        lintcode_url = 'http://www.lintcode.com/en/problem/{}/'.format(self._p_url_path)
        for url in [leetcode_url, lintcode_url]:
            response = requests.head(url)
            if response.status_code == 200:
                key_end = url.find('.com/')
                site = url[key_end - 8:key_end]
                self._p_urls[site] = url
        p_title = self._get_p_title()
        p_url_lists = []
        for site in sorted(self._p_urls):
            p_list = '- {site}: [{title}]({url})'.format(
                site=site, title=p_title, url=self._p_urls[site])
            p_url_lists.append(p_list)
        return p_url_lists

    def _get_p_title(self):
        """Get problem title."""
        p_title = self._raw_p_html('title').text().split('|')[0].strip()
        return p_title

    def _run_method(self, method):
        return getattr(self, '{}{}'.format(
            method,
            self._site))()

    def _get_p_html_body_leetcode(self):
        """Get problem html body only."""
        q_content_html = self._raw_p_html('.question-content').html()
        p_body_start = q_content_html.find('<p>')
        p_body_end = q_content_html.find('<div>')
        p_body = q_content_html[p_body_start:p_body_end]
        return p_body

    def _get_p_html_body_lintcode(self):
        q_content_html = self._raw_p_html('#description').html()
        p_body_end = q_content_html.find('<b>Tags</b>')
        p_body = q_content_html[:p_body_end]
        return p_body

    def _get_p_tags_leetcode(self):
        p_tags = []
        try:
            raw_tags = self._raw_p_html('.btn.btn-xs.btn-primary')
            for tag in raw_tags:
                if tag.attrib['href'].startswith('/tag/'):
                    p_tags.append(tag.text)
        except Exception as err:
            print('Error: ', err)
        return p_tags

    def _get_p_tags_lintcode(self):
        p_tags = []
        try:
            raw_tags = self._raw_p_html('#description')('#tags')('a')
            p_tags = [tag.text for tag in raw_tags]
        except Exception as err:
            print('Error: ', err)
        return p_tags

    def _get_p_difficulty_leetcode(self):
        difficulty_info = self._raw_p_html('.question-info.text-info')
        return difficulty_info.text().split(' ')[-1]

    def _get_p_difficulty_lintcode(self):
        raw_d_info = self._raw_p_html('.progress.progress-xs.m-b').html()
        d_info = raw_d_info.split('"Difficulty')[1].strip().split(' ')[0]
        return d_info

    def gen_markdown(self):
        """Generate markdown with problem html."""
        h = html2text.HTML2Text()
        if self._prefer_leetcode:
            self._lint2leet()
        p_title = self._get_p_title()
        p_body = self._run_method('_get_p_html_body_')
        p_difficulty = self._run_method('_get_p_difficulty_')
        raw_p_tags = self._run_method('_get_p_tags_')
        raw_p_tags.append(p_difficulty)
        p_tags = ['TAG_' + tag.replace(' ', '_') for tag in raw_p_tags]
        # markdown output
        lines = []
        lines.append('# {}\n'.format(p_title))
        tags = ' '.join(p_tags)
        lines.append('**TAGS:** {}\n'.format(tags))
        lines.append('## Question\n')
        p_url_lists = self._gen_p_url_lists()
        lines.extend(p_url_lists)
        lines.append('\n### Problem Statement\n')
        lines.append(h.handle(p_body))
        print('\n'.join(lines))


def main(argv):
    """Parse from html to markdown."""
    if (len(argv) == 2):
        scripts, url = argv
        prefer_leetcode = False
    elif (len(argv) == 3):
        scripts, url, prefer_leetcode = argv
    else:
        print("Usage: python ojhtml2markdown.py problem_url [prefer_leetcode]")
        sys.exit(1)
    ojhtml2markdown = OJHtml2Markdown(url, prefer_leetcode)
    ojhtml2markdown.gen_markdown()

if __name__ == "__main__":
    main(sys.argv)
