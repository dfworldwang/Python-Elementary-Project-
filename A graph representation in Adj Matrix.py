

class Graph(object):
    def __init__(self, edge_list):
        self.edge_list = edge_list

    def add_edge(self, edge_list):
        self.edge_list.append(edge_list)

    def adj_mtx(self):
        v = 0
        counter = set()
        for src, dest in self.edge_list:
            counter.add(src)
            counter.add(dest)

        v = len(counter)

        mtx = [[0 for y in range(v)]for x in range(v)]
        for e in self.edge_list:
            src, dest = e
            src = src - 1
            dest = dest - 1
            mtx[src][dest] = 1

        return mtx

edge_list = [(1,2), (2,3), (1,3)]
graph = Graph(edge_list)
mtx = graph.adj_mtx()

print(mtx)

assert mtx == [[0, 1, 1], [0, 0, 1], [0, 0, 0]]

graph.add_edge((3,3))
mtx = graph.adj_mtx()

print(mtx)

assert graph.adj_mtx() == [[0, 1, 1], [0, 0, 1], [0, 0, 1]]
