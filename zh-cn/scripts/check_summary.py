#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

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
            for l2 in os.listdir(level1):
                level2 = os.path.join(l1, l2)
                dir_file_list.append(level2)

    return dir_file_list


def get_summary_dir_file(summary_md):
    dir_file_list = []
    lines = open(summary_md)
    for line in lines:
        if line.find('* [') != -1:
            dir_file = re.split('[()]', line)[-2]
            dir_file_list.append(dir_file)

    return dir_file_list


def get_missing_summary(summary, dir_files):
    missing_lines = []
    for dir_file in dir_files:
        if dir_file not in summary:
            print("File %s was not added to SUMMARY.MD!!!" % dir_file)
            missing_lines.append(dir_file)

    return missing_lines


def fix_summary_md(root_dir, summary_md, missing_dir_files):
    summary_lines = open(summary_md).readlines()
    dir_index = []
    for line in summary_lines:
        if line.find('* [') != -1:
            dir_file = re.split('[()]', line)[-2]
            dir_name = os.path.dirname(dir_file)
            dir_index.append(dir_name)
        else:
            dir_index.append(line)

    for dir_file in missing_dir_files:
        dir_name = os.path.dirname(dir_file)
        # reverse find in list
        line_num = (len(dir_index) - 1) - dir_index[::-1].index(dir_name)
        title_prefix_index = summary_lines[line_num].find('* [')
        new_line = str(summary_lines[line_num][:title_prefix_index]) + '* ['
        title = get_title(os.path.join(root_dir, dir_file))
        if title == '':
            continue
        new_line += title + '](' + dir_file + ')' + '\n'
        summary_lines.insert(line_num + 1, new_line)
        dir_index.insert(line_num, dir_name)
        print("file %s has been added to SUMMARY.md" % dir_file)

    summary_output = open(summary_md, 'w')
    summary_output.writelines(summary_lines)
    summary_output.close()


def get_title(md_file):
    lines = open(md_file)
    title = ''
    for line in lines:
        if re.match('^# ', line):
            if re.search(' - ', line):
                title = re.split(' - ', line)[2:].rstrip()
            else:
                title = line[2:].rstrip()
            break

    return title


summ_dir_file = get_summary_dir_file(SUMMARY_MD)
sec_dir_file = get_dir_file(ROOT_DIR)
missing_dir_files = get_missing_summary(summ_dir_file, sec_dir_file)

fix_summary_md(ROOT_DIR, SUMMARY_MD, missing_dir_files)
