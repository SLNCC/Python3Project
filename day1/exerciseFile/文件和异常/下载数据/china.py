# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import pygal.maps.world


wm = pygal.maps.world.World()

wm.title = 'East Asia, Southeast Asia,South Asia,Central Asia and West Asia'

wm.add('East Asia', dict(cn=1338300000, kp=000, kr=4418000, jp=127451000, mn=2756000))

wm.add('Southeast Asia', ['vn', 'la', 'kh', 'mm', 'th', 'my', 'sg', 'ph', 'id','id','bn'])

wm.add('South Asia', ['pk', 'np', 'bt', 'in', 'bd', 'lk', 'mv'])

wm.add('Central Asia', ['kz', 'kg','uz', 'tj', 'tm', 'af'])

wm.add('West Asia', ['ir', 'iq', 'kw', 'sa', 'bh', 'qa', 'ae',
                     'om', 'ye', 'jo', 'il', 'sy', 'lb', 'cy', 'tr', 'az','ge', 'am', 'ps'])

wm.render_to_file('china.svg')