Here is an example on how Breadth First Search works on a graph of nodes: 




class Node: 
  def __init__(self, val, neighbors = []):
    self.val = val
    self.neighbors = neighbors

def bfs(s):
  seen = set() 
  queue = []

  seen.add(s)
  queue.append(s)

  while queue:
    cur = queue.pop(0)
    doWork(cur.val)
    for neighbor in cur.neighbors:
      if neighbor not in seen:
        queue.append(neighbor)
        seen.add(neighbor)

def doWork(n):
  print(n)

a = Node('A')
e = Node('E')
d = Node('D')
c = Node('C')
b = Node('B')
g = Node('G')
f = Node('F')
h = Node('H')

a.neighbors = [b,e,d,c]
e.neighbors = [f,a,d]
d.neighbors = [a,e,h,c]
c.neighbors = [a,d,b]
b.neighbors = [g,a,c]
g.neighbors = [b,f]
f.neighbors = [g,e,h]
h.neighbors = [f,d]

bfs(a)