#!/usr/bin/env python3
"""Parse Leetcode/Lintcode html page to markdown."""

import frontmatter
import requests
import html2text


class YamlContent(object):
    def __init__(self, metadata, content):
        self.metadata_ = metadata
        self.content_ = content
    
    @property
    def metadata(self):
        return self.metadata_
    
    @property
    def content(self):
        return self.content_

        content = '# ' + title
        yaml_content = YamlContent(metadata, content)


def leet_lint_url(url):
    problem_slug = url.strip('/').split('/')[-1]
    leetcode_url = 'https://leetcode.com/problems/{}/'.format(problem_slug)
    lintcode_url = 'https://www.lintcode.com/problem/{}/'.format(problem_slug)
    urls = {}
    for url in [leetcode_url, lintcode_url]:
        response = requests.head(url)
        if response.status_code != 404:
            if url.startswith('https://leetcode'):
                urls['leetcode'] = url
            elif url.startswith('https://www.lintcode'):
                urls['lintcode'] = url
        else:
            print('cannot find url with: {}'.format(url))
    return urls


def problem2md(problem, convert_desc=True):
    metadata = {
        'title': problem['title'],
        'difficulty': problem['difficulty']
    }
    if problem['tags']:
        metadata['tags'] = problem['tags']

    description = problem['description']
    description_md = description
    if convert_desc:
        h = html2text.HTML2Text()
        description_md = h.handle(description)

    lines = []
    lines.append('# ' + problem['title'] + '\n')
    lines.append('## Problem\n')
    lines.append('### Metadata\n')
    if problem['tags']:
        lines.append('- tags: ' + ', '.join(problem['tags']))
    lines.append('- difficulty: ' + problem['difficulty'])
    urls = leet_lint_url(problem['url'])
    for k, v in urls.items():
        lines.append('- source({}): <{}>'.format(k, v))
    lines.append('\n### Description\n')
    lines.append(description_md)

    content = '\n'.join(lines)
    yaml_content = YamlContent(metadata, content)
    problem_md = frontmatter.dumps(yaml_content, allow_unicode=True)
    return problem_md
