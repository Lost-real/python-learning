#!/usr/bin/python
# -*- coding: utf-8 -*-
# conda activate python3
"""
    作者：徐诗芬
    内容：读取并输出所有blast结果中最好的第一条hit结果
    日期：2021.1.22
"""
import sys

def usage():
    print('Usage: python blast_best.py [input_file] [outfile]')


def main():

    # global name
    inf = open(sys.argv[1], 'rt')
    ouf = open(sys.argv[2], 'wt')

    flag_list = []
    for line in inf:
        line = line.strip()
        name = line.split("\t")[0]
        #id = eval(line.split("\t")[2])
        if name not in flag_list:
            ouf.write(line + '\n')
        else:
            continue
        flag_list.append(name)

    inf.close()
    ouf.close()

try:
    main()
except IndexError:
    usage()
