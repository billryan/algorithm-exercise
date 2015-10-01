#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from jinja2 import Template
from subprocess import check_output

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


def sitemap(suffix='.md'):
    # ensure we are in the ROOT_DIR
    os.chdir(ROOT_DIR)
    multilang = ['en/', 'zh-cn/', 'zh-tw/']
    pages = []
    raw_bytes = check_output('scripts/gitls.sh')
    # ignore last blank string
    raw_strs = raw_bytes.decode("utf-8").split('\n')[:-1]
    for raw_str in raw_strs:
        date, raw_f = raw_str.split(' ')
        for lang in multilang:
            if raw_f.startswith(lang) and raw_f.endswith(suffix):
                if raw_f == lang + 'SUMMARY.md':
                    continue
                p = Path(raw_f)
                # rename README with index
                if p.name == 'README.md':
                    p = p.with_name('index.md')
                p = p.with_suffix('.html')
                fn = p.as_posix().lower()
                page = {}
                page['date'] = date
                page['url'] = fn
                pages.append(page)
    root_url = 'http://algorithm.yuanbin.me'
    template = Template(os.path.join(BASE_DIR, 'sitemap.xml'))
    template.render(root_url=root_url, pages=pages)
    # print(sitemap_xml)


if __name__ == "__main__":
    sitemap()
