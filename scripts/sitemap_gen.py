#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from jinja2 import Template

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


def sitemap(suffix='md'):
    # ensure we are in the ROOT_DIR
    os.chdir(ROOT_DIR)
    multilang = ['en', 'zh-cn', 'zh-tw']
    pages = []
    for lang_dir in multilang:
        for p in Path(lang_dir).glob('**/*.' + suffix):
            # rename README with index
            if p.name == 'README.md':
                p.with_name('index.md')
            p.with_suffix('.html')
            fn = p.as_posix().lower()
            pages.append(fn)

    root_url = 'http://algorithm.yuanbin.me'
    template = Template(os.path.join(BASE_DIR, 'sitemap.xml'))
    sitemap_xml = template.render(root_url=root_url, pages=pages)


if __name__ == "__main__":
    print("test")
