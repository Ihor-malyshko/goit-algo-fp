from collections import deque
from task4 import Node, draw_tree


def generate_colors(n):
  colors = []
  for i in range(n):
    intensity = int(255 - (255 * i / (n - 1))) if n > 1 else 255
    color = f"#{intensity:02x}{intensity:02x}{255:02x}"
    colors.append(color)
  return colors


def dfs_traversal(root):
  if not root:
    return []
  
  visited = []
  stack = [root]
  
  while stack:
    node = stack.pop()
    visited.append(node)
    
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  
  return visited


def bfs_traversal(root):
  if not root:
    return []
  
  visited = []
  queue = deque([root])
  
  while queue:
    node = queue.popleft()
    visited.append(node)
    
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  
  return visited


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# глибину обхід
dfs_order = dfs_traversal(root)
colors = generate_colors(len(dfs_order))
for i, node in enumerate(dfs_order):
  node.color = colors[i]

draw_tree(root)

# ширину обхід
bfs_order = bfs_traversal(root)
colors = generate_colors(len(bfs_order))
for i, node in enumerate(bfs_order):
  node.color = colors[i]

draw_tree(root)
