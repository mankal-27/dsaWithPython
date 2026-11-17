import os
import sys

base = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(base, 'input.txt'), 'r')
sys.stdout = open(os.path.join(base, 'output.txt'), 'w')


def string_length(str):
    cnt = 0
    for chr in str:
        cnt = cnt + 1
    return cnt

name = "manjunath"
print(len(name))
print(string_length(name))
