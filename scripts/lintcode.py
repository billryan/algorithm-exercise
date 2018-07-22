#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from pyquery import PyQuery as pq
import requests


class Lintcode(object):

    def __init__(self):
        self.driver = None

    def open_url(self, url):
        print('open URL: {}'.format(url))
        url = url.strip('description')
        url = url.strip('/')
        self.url = url
        lintcode_unique_name = url.split('/')[-1]
        req_url = 'https://www.lintcode.com/api/problems/detail/?unique_name_or_alias={}&_format=detail'.format(lintcode_unique_name)
        self.driver = requests.get(req_url).json()

    def get_title(self):
        print('get title...')
        title = self.driver['title']
        return title

    def get_description(self):
        print('get description...')
        desc = self.driver['description']
        notice = self.driver['notice']
        clarification =  self.driver['clarification']
        example = self.driver['example']
        challenge = self.driver['challenge']
        desc_full = desc
        if notice:
            desc_full += '\n\n#### Notice\n\n' + notice
        if clarification:
            desc_full += '\n\n#### Clarification\n\n' + clarification
        if example:
            desc_full += '\n\n#### Example\n\n' + example
        if challenge:
            desc_full += '\n\n#### Challenge\n\n' + challenge

        return desc_full

    def get_difficulty(self):
        print('get difficulty...')
        mapping = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
        difficulty = mapping.get(self.driver['level'], 'unknown')
        return difficulty

    def get_tags(self):
        print('get tags...')
        tags = []
        for i in self.driver['tags']:
            if i['alias']:
                tags.append(i['alias'])
            else:
                tags.append(i['name'])
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
            'url': self.url
        }
        return problem


if __name__ == '__main__':
    url = 'https://www.lintcode.com/problem/topological-sorting'
    lintcode = Lintcode()
    print(lintcode.get_problem_all(url))
