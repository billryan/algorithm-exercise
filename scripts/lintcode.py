#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyquery import PyQuery as pq


class Lintcode(object):

    def __init__(self):
        self.driver = None

    def open_url(self, url):
        self.url = url
        print('open URL: {}'.format(url))
        self.driver = pq(url=url)

    def get_title(self):
        print('get title...')
        title = self.driver('title').text()
        return title

    def get_description(self):
        print('get description...')
        desc_pq = self.driver('#description')
        desc_html = desc_pq('.m-t-lg:nth-child(1)').html()
        example_html = desc_pq('.m-t-lg:nth-child(2)').html()
        return desc_html + example_html

    def get_difficulty(self):
        print('get difficulty...')
        progress_bar = self.driver('.progress-bar')
        original_title = progress_bar.attr('data-original-title')
        splits = original_title.strip().split(' ')
        difficulty = splits[1]
        ac_rate = splits[-1]
        return difficulty

    def get_tags(self):
        print('get tags...')
        tags = []
        for i in self.driver('#tags.tags a'):
            tags.append(i.text)
        return tags

    def _get_related(self):
        print('get related...')
        related = self.driver('.m-t-lg:last')
        return related

    def _clean_url(self, url):
        new_url = ['http:/', 'www.lintcode.com', 'en/problem']
        problem_slug = url[len('http://'):].strip('/').split('/')[3]
        new_url.append(problem_slug)
        return '/'.join(new_url)

    def get_problem_all(self, url):
        """获取所有细节"""
        print('get all the problem detail...')
        self.open_url(url)
        title = self.get_title()
        difficulty = self.get_difficulty()
        tags = self.get_tags()
        description = self.get_description()
        problem = {
            'title': title,
            'difficulty': difficulty,
            'tags': tags,
            'description': description,
            'url': self._clean_url(url)
        }
        return problem


if __name__ == '__main__':
    url = 'http://www.lintcode.com/en/problem/palindrome-number/'
    leetcode = Lintcode()
    print(leetcode.get_problem_all(url))
