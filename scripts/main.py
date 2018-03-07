#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from datetime import datetime

from util import par_dir, mkdir_p
from leetcode import Leetcode
from ojhtml2markdown import problem2md

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def curr_time():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper for GitBook algorithm')
    parser.add_argument('--new', type=str, dest='new',
                        help='create new post with given leetcode/lintcode url.')
    parser.add_argument('--update', nargs='*', dest='update',
                        help='update post with given title in post and summary.')
    parser.add_argument('--migrate', type=str, dest='migrate',
                        help='migrate old posts.')
    parser.add_argument('--fix-summary', dest='fix_summary',
                        help='render new summary from posts.')
    args = parser.parse_args()
    print('Called with arguments: {}'.format(args))

    ROOTDIR = par_dir(BASEDIR)
    raw_url = args.new
    if raw_url.startswith('https://leetcode'):
        leetcode = Leetcode()
        problem = leetcode.get_problem_all(raw_url)
        problem_md = problem2md(problem)
        print(problem_md)