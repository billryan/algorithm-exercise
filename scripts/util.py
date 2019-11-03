#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def par_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))