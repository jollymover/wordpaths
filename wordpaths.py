#!/usr/bin/env python

import sys

def get_subdict(file_name, length):
    subdict = []
    with open(file_name, 'r') as file:
        for line in file:
            item = line[:-1]
            if len(item) == length:
                subdict.append(item)
    file.close
    return subdict

def compare(str1, str2):
    matches = 0
    for i in range (0, len(str1)):
        if str1[i] == str2[i]:
            matches += 1
    return matches

def get_graph(dic):
    graph = []
    length = len(dic[0])
    for i in range(0, len(dic)):
        graph.append([])
        for j in range(0, len(dic)):
            if compare(dic[i], dic[j]) == length - 1:
                graph[i].append(j)
    return graph

def fire_graph(graph, start):

    mark = []
    prior = []
    queue = []

    for i in range(0, len(graph)):
        mark.append(0)
        prior.append(-1)

    queue.insert(0, start)
    mark[start] = 1
    prior[start] = -1
    while len(queue) > 0:
        v = queue.pop(0)
        for i in range(0, len(graph[v])):
            to = graph[v][i]
            if mark[to] == 0:
                mark[to] = 1
                queue.append(to)
                prior[to] = v
    return mark, prior

def main():

    path = []

    # Check and parse CLI arguments
    if len(sys.argv) < 4:
        print "Usage: wordpath.py path word1 word2"
        sys.exit(1)
    elif sys.argv[2] == sys.argv[3]:
        print "Error: the same word is used twice"
        sys.exit(1)
    elif len(sys.argv[2]) != len(sys.argv[3]):
        print "Error: words must be of equal length"
        sys.exit(1)

    dict_file_name = sys.argv[1]
    subdict = get_subdict(dict_file_name, len(sys.argv[2]))
    graph = get_graph(subdict)

    try:
        start = subdict.index(sys.argv[2])
        finish = subdict.index(sys.argv[3])
    except ValueError:
        print "Error: Words not found in dictionary"
        sys.exit(1)

    mark, prior = fire_graph(graph, start)

    if mark[finish] == 0:
        print "No path"
    else:
        v = finish
        path.append(v)
        while v != -1:
            v = prior[v]
            path.append(v)

    path.pop()
    path.reverse()
    for v in range(0, len(path) - 1):
        print subdict[path[v]], '->',
    print subdict[path[-1]]

    sys.exit(0)

if __name__ == "__main__":
    main()
