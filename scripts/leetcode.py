#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver


class Leetcode(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def open_url(self, url):
        self.url = url
        print('open URL: {}'.format(url))
        self.driver.get(url)

    def teardown(self):
        self.driver.close()

    def get_title(self):
        print('get title...')
        raw_title = self.driver.title
        title = raw_title[:-len(' - LeetCode')].strip()
        return title

    def get_description(self):
        print('get description...')
        elem = self.driver.find_element_by_class_name('question-description')
        return elem.get_attribute('innerHTML')
    
    def get_difficulty(self):
        print('get difficulty...')
        elem = self.driver.find_element_by_class_name('difficulty-label')
        return elem.get_attribute('innerHTML')

    def get_tags(self):
        print('get tags...')
        tags_id = self.driver.find_element_by_id('tags-topics')
        tags_id_a = tags_id.find_elements_by_tag_name('a')
        tags = []
        for i in tags_id_a:
            tag = i.get_attribute('innerHTML')
            tags.append(tag)
        return tags
    
    def _clean_url(self, url):
        new_url = ['https:/', 'leetcode.com', 'problems']
        problem_slug = url[len('https://'):].strip('/').split('/')[2]
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
        self.teardown()
        return problem


if __name__ == '__main__':
    url = 'https://leetcode.com/problems/palindrome-number'
    leetcode = Leetcode()
    print(leetcode.get_problem_all(url))
