# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

#
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = first + ' ' + last
#     return full_name.title()


def get_formatted_name(first,middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' +middle + '' + last
    return full_name.title()