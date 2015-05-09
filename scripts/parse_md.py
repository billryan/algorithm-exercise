#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

class parseMD:
    def __init__(self, fname, isSummary=False):
        self.fname = fname
        self.isSummary = isSummary

    def get_title(self):
        lines = open(self.fname)
        for line in lines:
            if re.match('^# ', line):
                title = re.split(' - ', line)[2:]
                break

        return title
