from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break
    nodes.remove(min_node)
    current_weight = visited[min_node]
    for edge in graph.edges[min_node]:
      #print(visited)
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
    
  return visited



if __name__ == '__main__':

    matrix_filename = input('Please provide a filename containing an adjacency list:\n')
    with open(matrix_filename, 'r') as matrix_file:
        nodes = [line.strip() for line in matrix_file.readlines()]
    graph = Graph()
    for node in nodes:
        connections = node.split()
        graph.add_node(connections[0])
    for node in nodes:
        connections = node.split()
        for i in range(1,len(connections)):
            edge_and_weight = connections[i].split(",")
            graph.add_edge(connections[0],edge_and_weight[0],int(edge_and_weight[1]))
    start_vertex = input("Please provide a start vertex label (1..n):\n")
    #print(graph.distances)
    path_lengths = dijkstra(graph,start_vertex)
    out_string = ''
    for i in range(1,len(path_lengths)+1):
        if i < len(path_lengths):
            out_string += str(path_lengths[str(i)]) + ','
        else:
            out_string += str(path_lengths[str(i)])
    print(out_string)