import maze as mz
import queue
import math

maze = ""
maze += "+---+---+---+\n"  
maze += "|           |\n" # row0
maze += "+   +---+   +\n"
maze += "|     * |   |\n" # row1
maze += "+---+   +   +\n"
maze += "| X         |\n" # row2
maze += "+---+---+---+\n"

maze = mz.Maze(maze, 14)

class Node:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
    
  def add_neighbor(self, neighbor, cost):
    self.neighbors.append((neighbor, cost))
    
  def __lt__(self, node2):
    return self.key < node2.key
    
  def __str__(self):
    STRING = ''
    STRING += 'Key: ' + self.key + '\n'
    for i in self.neighbors:
      STRING += 'Neighbor '+ i[0].key + ' , ' + str(i[1]) + '\n'
      
    return STRING
    
  

class Graph:
  def __init__(self):
    self.nodes = {}
    
  def add_node(self, node):
    self.nodes[node.key] = node
    
  def add_edge(self, node, neighbor, cost):
    node.add_neighbor(neighbor, cost)
    neighbor.add_neighbor(node, cost)
    
  def __str__(self):
    STRING = ''
    for i in self.nodes:
      STRING += self.nodes[i].__str__() + '\n'
    return STRING
    
  def get_dfs_path(self, currentNode, end, vis, path):
    vis.append(currentNode)
    if currentNode == end:
      return path
    for i in currentNode.neighbors:
      if i[0] not in vis:
        np = self.get_dfs_path(i[0], end, vis, path + [i[0].key])
        
        if np != None:
          return np
          
  def get_bfs_path(self, start_node, end_node):
    queue = [(start_node, [start_node.key])]
    vis = [start_node]
    while len(queue) != 0:
      p = queue.pop(0)
      popped = p[0]
      if popped == end_node:
        return p[1]
      for i in popped.neighbors:
        if i not in vis:
          vis.append(i[0])
          queue.append((i[0], p[1] + [i[0].key]))
          
          
  def get_dls_path(self, currentNode, end_node, depth_limit, localDepth, vis, path):
    vis.append(currentNode)
    if currentNode == end_node:
      return path
    elif localDepth > depth_limit:
      return
  
    for i in currentNode.neighbors:
      if i[0] not in vis:
        localDepth += 1
        newP = self.get_dls_path(i[0], end_node, depth_limit, localDepth, vis, path + [i[0].key])
        
        if newP != None:
          return newP
      
    
    
  def get_ids_path(self, start_node, end_node, max_depth):
    localDepth = 0
    for i in range(0, max_depth+1):
      vis, path = [], [n00.key]
      DLS_Path = self.get_dls_path(n00, n20, i, localDepth, vis, path)
      if DLS_Path != None:
        return DLS_Path
        
  
        
  def get_ucs_path(self, start_node, end_node):
    
    q = queue.PriorityQueue()
    q.put((0, start_node, [start_node.key]))
    vis = []
    while q.empty() == False:
      n = q.get()
      if n[1] not in vis:
        vis.append(n[1])
        if n[1] == end_node:
          return n[2]
        for i in n[1].neighbors:
          if i[0] not in vis: 
            q.put((i[1] + n[0], i[0], n[2]+[i[0].key]))
          
n00 = Node('(0,0)')
n01 = Node('(0,1)')
n02 = Node('(0,2)')

n10 = Node('(1,0)')
n11 = Node('(1,1)')
n12 = Node('(1,2)')

n20 = Node('(2,0)')
n21 = Node('(2,1)')
n22 = Node('(2,2)')

g = Graph()
g.add_node(n00)
g.add_node(n01)
g.add_node(n02)

g.add_node(n10)
g.add_node(n11)
g.add_node(n12)

g.add_node(n20)
g.add_node(n21)
g.add_node(n22)

g.add_edge(n00, n10, 1)
g.add_edge(n00, n01, 1)
g.add_edge(n01, n02, 1)
g.add_edge(n10, n11, 10)
g.add_edge(n11, n21, 1)
g.add_edge(n21, n20, 1)
g.add_edge(n02, n12, 1)
g.add_edge(n12, n22, 1)
g.add_edge(n22, n21, 1)


vis = []
path = [n00.key]
DFS_Path = g.get_dfs_path(n00, n20, vis, path)
maze.print_path(DFS_Path)
print('\n ______________________________ \n')
BFS_Path = g.get_bfs_path(n00, n20)
maze.print_path(BFS_Path)
print('\n ______________________________ \n')
localDepth = 0
vis, path = [], [n00.key]
IDS_Path = g.get_ids_path(n00, n20, 4)
maze.print_path(IDS_Path)
print('\n ______________________________ \n')
UCS_Path = g.get_ucs_path(n00, n20)
maze.print_path(UCS_Path)
