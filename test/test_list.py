#!/usr/bin/env python

import cProfile

# test build list by same value 
cProfile.run("l = [0] * 100000000")
cProfile.run("l = [0 for i in range(100000000) ]")
cProfile.run("l = [0 for i in xrange(100000000)]")

