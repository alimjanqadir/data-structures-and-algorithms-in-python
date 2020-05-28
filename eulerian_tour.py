# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that have an Eulerian tour.
#


def create_tour(nodes):
    # your code here
    tour = []
    first_node = nodes[0]
    for x in xrange(0, len(nodes)):
        if x < len(nodes) - 1:
            tour.append((nodes[x], nodes[x + 1]))
        else:
            tour.append((nodes[x], first_node))
    return tou

#########


def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree


def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None


def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes


def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def find_eulerian_tour(graph):
    tour = []

    if len(graph) == 0:
        return []

    # Set up intial path for eulerian tour,
    # for loop below searches the trailing path.
    if len(tour) == 0:
        initial_edge = graph.pop(0)
        tour.append(initial_edge[0])
        tour.append(initial_edge[1])

    # Use recursive helper function to find the tour.
    return find_eulerian_tour_helper(graph, tour)


def find_eulerian_tour_helper(graph, tour):
    # is_found flag indicates whether targeted edge is found,
    # and used to end recurisve function.
    is_found = False

    for x in xrange(len(graph)):
        edge = graph[x]
        from_node = edge[0]
        to_node = edge[1]

        previous_node_in_tour = tour[len(tour) - 1]

        if (previous_node_in_tour != from_node and
                previous_node_in_tour != to_node):
            continue

        if previous_node_in_tour == from_node:
            tour.append(to_node)
            graph.pop(x)
            is_found = True
            break
        elif previous_node_in_tour == to_node:
            tour.append(from_node)
            graph.pop(x)
            is_found = True
            break

    if is_found:
        return find_eulerian_tour_helper(graph, tour)
    else:
        return tour

print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])

print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])

