import doctest
import networkx as nx


def vcg_cheapest_path(graph, source, target):
    """
    >>> g=nx.Graph()
    >>> g.add_edge('a','b',weight=3)
    >>> g.add_edge('a','c',weight=5)
    >>> g.add_edge('a','d',weight=10)
    >>> g.add_edge('b','c',weight=1)
    >>> g.add_edge('b','d',weight=4)
    >>> g.add_edge('c','d',weight=1)
    >>> vcg_cheapest_path(g,'a','d')
    cost of edge (a,b):4
    cost of edge (a,c):0
    cost of edge (a,d):0
    cost of edge (b,c):2
    cost of edge (b,d):0
    cost of edge (c,d):3
    total paymetn:9

    """
    path_weight, path = nx.single_source_dijkstra(graph, source, target, weight='weight')  # path is list of node in the path,
    total_payment = 0
    for edge in graph.edges:
        edge_weight = graph[edge[0]][edge[1]]['weight']
        graph.remove_edge(edge[0], edge[1])
        temp_weight, temp_path = nx.single_source_dijkstra(graph, source, target, weight='weight')
        if temp_weight == path_weight:
            payment = 0
        else:
            payment = temp_weight - path_weight + edge_weight
        print("cost of edge (" + edge[0] + "," + edge[1] + "):" + str(payment))
        graph.add_edge(edge[0], edge[1], weight=edge_weight)
        total_payment += payment
    print("total paymetn:" + str(total_payment))


if __name__ == '__main__':
    doctest.testmod(name='vcg_cheapest_path', verbose=True)
