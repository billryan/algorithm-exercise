#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import parse_md

reserve_name = ['source_code', 'scripts', 'docs', 'conf', 'images',
                '_book', 'node_modules', '.git', '.DS_Store']
level_prefix = {'* ', '   * ', '       * '}
SUMMARY_MD = '../SUMMARY.md'
ROOT_DIR = '..'


def get_dir_file(root_dir):
    dir_file_list = []
    # level 1
    for l1 in os.listdir(root_dir):
        level1 = os.path.join(root_dir, l1)
        if os.path.isdir(level1) and l1 not in reserve_name:
            print("l1: %s" % l1)
            for l2 in os.listdir(level1):
                level2 = os.path.join(l1, l2)
                dir_file_list.append(level2)

    return dir_file_list


def get_summary_dir_file(summary_md):
    dir_file_list = []
    lines = filter(None, (line.rstrip() for line in open(summary_md)))
    for line in lines:
        if line and line.lstrip()[0] == '*':
            dir_file = re.split('[()]', line)[-2]
            dir_file_list.append(dir_file)

    return dir_file_list


def fix_summary(summary, dir_files):
    for dir_file in dir_files:
        if dir_file not in summary:
            print("File %s was not added to SUMMARY.MD!!!" % dir_file)


def get_title(fname):
    lines = open(fname)
    for line in lines:
        if re.match('^# ', line):
            title = re.split(' - ', line)[2:]
            break

    return title


summ_dir_file = get_summary_dir_file(SUMMARY_MD)
sec_dir_file = get_dir_file(ROOT_DIR)

fix_summary(summ_dir_file, sec_dir_file)
