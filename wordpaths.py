#!/usr/bin/env python

import sys

def get_subdict(file_name, length):
    """Extracts all words of appropriate length from source dictionary.

    :param file_name: The source dictionary path
    :param length: The length of words to be extracted
    :returns: Subdict (list)
    """
    subdict = []
    with open(file_name, 'r') as file:
        for line in file:
            item = line[:-1]
            if len(item) == length:
                subdict.append(item)
    file.close
    return subdict

def compare(str1, str2):
    """Compare simbols in two strings

    :param str1: The first comparable string
    :param str2: The second comparable string
    :returns: Number of matched symbols
    """
    matches = 0
    for i in range (0, len(str1)):
        if str1[i] == str2[i]:
            matches += 1
    return matches

def get_graph(dic):
    """Converts the dict to graph

    :param dict: The source dict
    :returns: Graph as two-dimension list
    """
    graph = []
    length = len(dic[0])
    for i in range(0, len(dic)):
        graph.append([])
        for j in range(0, len(dic)):
            if compare(dic[i], dic[j]) == length - 1:
                graph[i].append(j)
    return graph

def fire_graph(graph, start):
    """Finds pathes in the graph

    :param graph: The source graph
    :param start: The start vertice
    :returns: Array of marks for each vertice (is it available from start
    vertice) and array of priors (previos vertice for each array on the path)
    """
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
        vert = queue.pop(0)
        for i in range(0, len(graph[vert])):
            to = graph[vert][i]
            if mark[to] == 0:
                mark[to] = 1
                queue.append(to)
                prior[to] = vert
    return mark, prior

def main():
    """Print word path in dictionary as:

    wordpaths.py /usr/share/dict/words cat dog
    cat -> cag -> cog -> dog

    :param argv[1]: The path to dictionary file
    :param argv[2]: The start word
    :param argv[3]: The finish word
    """
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
        vert = finish
        path.append(vert)
        while vert != -1:
            vert = prior[vert]
            path.append(vert)

    path.pop()
    path.reverse()
    for vert in range(0, len(path) - 1):
        print subdict[path[vert]], '->',
    print subdict[path[-1]]

    sys.exit(0)

if __name__ == "__main__":
    main()
