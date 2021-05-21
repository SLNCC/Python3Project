# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import unittest

from name_function import get_formatted_name


class NamesTextCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Qiao Dd这样的姓名吗？"""
        formatted_name = get_formatted_name('qiao','dd')
        self.assertEqual(formatted_name,'Qiao Dd')

unittest.main()