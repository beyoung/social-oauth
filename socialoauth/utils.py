# -*- coding: utf-8 -*-
import sys


def get_python_version():
    """
    check python version
    :return:
    """
    return sys.version_info[0]


def import_oauth_class(m):
    m = m.split('.')
    c = m.pop(-1)
    module = __import__('.'.join(m), fromlist=[c])
    return getattr(module, c)
