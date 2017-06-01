#!/usr/bin/env python

import wordpaths
import unittest
from subprocess import check_output

class TestStringMethods(unittest.TestCase):

    def test_get_subdict(self):
        return wordpaths.get_subdict('test_dic', 3) == ['cat', 'cag', 'cog']

    def test_compare(self):
        str1 = 'cat'
        str2 = 'cag'
        return wordpaths.compare(str1, str2) == 2

    def test_get_graph(self):
        dic = ['cat', 'cag', 'cog']
        return wordpaths.get_graph(dic) == [[1], [0, 2], [1]]

    def test_fire_graph(self):
        dic = ['cat', 'cag', 'cog']
        graph = wordpaths.get_graph(dic)
        mark, prior = wordpaths.fire_graph(graph, 0)
        return mark == [1, 1, 1] and prior == [-1, 0, 1]

    def test_wordpaths(self):
        return check_output(['./wordpaths.py', 'test_dic', 'cat', 'cog']) == 'cat -> cag -> cog'

if __name__ == '__main__':
    unittest.main()
