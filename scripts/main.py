#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from datetime import datetime

import frontmatter
from slugify import slugify

from util import par_dir, mkdir_p
from leetcode import Leetcode
from lintcode import Lintcode
from summary import update_summary
from ojhtml2markdown import problem2md

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def curr_time():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper for GitBook algorithm')
    parser.add_argument('--new', type=str, dest='new',
                        help='create new post with given leetcode/lintcode url.')
    parser.add_argument('--dir', type=str, dest='dir',
                        help='create md under dir.')
    parser.add_argument('--update', nargs='*', dest='update',
                        help='update post with given title in post and summary.')
    parser.add_argument('--migrate', type=str, dest='migrate',
                        help='migrate old posts.')
    parser.add_argument('--fix-summary', dest='fix_summary',
                        help='render new summary from posts.')
    args = parser.parse_args()
    print('Called with arguments: {}'.format(args))

    ROOTDIR = par_dir(BASEDIR)
    if args.new:
        raw_url = args.new
        problem_md = ''
        problem_slug = ''
        xxxcode = None
        convert_desc = True
        if raw_url.startswith('https://leetcode'):
            xxxcode = Leetcode()
        elif raw_url.startswith('https://www.lintcode.com'):
            xxxcode = Lintcode()
            convert_desc = False
        problem = xxxcode.get_problem_all(raw_url)
        problem_slug = slugify(problem['title'], separator="_")
        problem_md = problem2md(problem, convert_desc)

    if args.dir:
        post_dir = os.path.join(ROOTDIR, args.dir)
        post_fn = os.path.join(post_dir, problem_slug + '.md')
        summary_path = args.dir.strip('/').split('/')[-1] + '/' + problem_slug + '.md'
        summary_line = '* [{title}]({path})'.format(title=problem['title'], path=summary_path)
        print(summary_line)
        mkdir_p(post_dir)
        with open(post_fn, 'w', encoding='utf-8') as f:
            print('create post file {}...'.format(post_fn))
            f.write(problem_md)
    
    if args.fix_summary:
        update_summary(ROOTDIR)