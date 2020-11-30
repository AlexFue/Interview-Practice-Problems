This algorithm is for depth wise searches of a tree or graph 




class Node: 
  def __init__(self, val, neighbors = []):
    self.val = val
    self.neighbors = neighbors

def dfs(s):
  seen = set() 
  def helper(node):
    if node not in seen: 
      doWork(node.val)
      seen.add(node)
      for neighbor in node.neighbors:
        helper(neighbor)
  helper(s)

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

dfs(a)


