# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import pprint
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# pprint.pprint(printBoard(theBoard))


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
         turn = 'O'
    else:
         turn = 'X'


printBoard(theBoard)