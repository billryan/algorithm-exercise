#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from shutil import copyfile
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from subprocess import check_output

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


def sitemap(suffix='.md'):
    # ensure we are in the ROOT_DIR
    os.chdir(ROOT_DIR)
    multilang = ['en/', 'zh-hans/', 'zh-tw/']
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
                page['lastmod'] = date
                page['url'] = fn
                pages.append(page)
    root_url = 'http://algorithm.yuanbin.me'
    templates = os.path.join(BASE_DIR, 'sitemap' + os.sep + 'templates')
    env = Environment(loader=FileSystemLoader(templates))
    template = env.get_template('sitemap.xml')
    sitemap_xml = template.render(root_url=root_url, pages=pages, freq='daily')
    sitemap_fn = os.path.join(ROOT_DIR, 'sitemap.xml')
    with open(sitemap_fn, 'w') as sf:
        sf.write(sitemap_xml)
    sitemap_txt_fn = os.path.join(ROOT_DIR, 'sitemap.txt')
    with open(sitemap_txt_fn, 'w') as sf:
        urls = [root_url + '/' + page['url'] + '\n' for page in pages]
        sf.writelines(urls)
    # gitbook do not serve static files under root dir
    sitemap_en_fn = os.path.join(ROOT_DIR, 'en' + os.sep + 'sitemap.xml')
    copyfile(sitemap_fn, sitemap_en_fn)


if __name__ == "__main__":
    sitemap()
