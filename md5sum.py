#!/usr/bin/env python
# coding=utf-8
#
#  Copyright (c) 2014 Zhong Kaixiang
#
#  @file     md5sum.py
#  @author   kaka_ace <xiang.ace@gmail.com>
#  @date     Thu Nov 06 2014
#  @brief    caculate md5 value    
#            require Crypto 
#          

import sys 
if len(sys.argv) < 2:
    print(" Usage: md5sum.py [file] or stdin stream")

from optparse import OptionParser 

usage = "usage: %prog [options] arg"  
parser = OptionParser(usage)  
parser.add_option("-f", "--file", dest="filename",  
                      help="read data from FILENAME, \
if -s/--stdin is set, the -f/--file does not work")  

parser.add_option("-s", "--stdin", dest="stdin",
                      help="read data from STDIN")
parser.add_option("-v", "--verbose",  
                      action="store_true", dest="verbose")  
parser.add_option("-q", "--quiet",  
                      action="store_false", dest="verbose")  

(options, args) = parser.parse_args() # default parameter is sys.argv[1:] 

if options.filename is None and options.stdin is None:
    print("not enough parameters!!!")
    sys.exit(1)

# caculate md5 value 
from Crypto.Hash import MD5

def caculate_md5_value_from_string(s):
    """

    """
    m = MD5.new(s)
    return m.hexdigest()

def caculate_md5_value_from_filename(filename):
    """

    """
    _READ_FILE_BUFFER = 10240
    try:
        f = open(filename, "rb")
    except Exception:
        print("could not operation file: %s" % options.filename)
        return None 

    m = MD5.new()
    while True:
        buf = f.read(_READ_FILE_BUFFER)
        if buf == "":
            break
        m.update(buf)
    f.close()
    return m.hexdigest()

if __name__ == "__main__":
    from functools import partial

    if not (options.stdin is None):
        md5sum_func = partial(caculate_md5_value_from_string, options.stdin)   
    else: # read from file
        md5sum_func = partial(caculate_md5_value_from_filename, options.filename)

    md5_value = md5sum_func()
    if md5_value is None:
        sys.exit(1)
    print(md5_value)
    sys.exit(0)

