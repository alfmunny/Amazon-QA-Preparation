class TreeNode:
  def __init__(self, val=1, left=None, right=None):
    self.val= val
    self.left = left
    self.right = right

def distance_between_nodes(arr, node1, node2):

  root = build_bst(arr)

  ancestor = LCA(root, node1, node2)

  ds1 = distance(root, node1)
  ds2 = distance(root, node2)

  return ds1 + ds2


def build_bst(arr):
  root = None
  for v in arr:
    root = insert_bst(root, v)

  return root

def insert_bst(root, v):
  if not root:
    return TreeNode(v)
  if not v:
    return root

  if v > root.val:
    root.right = insert_bst(root.right, v)
  else:
    root.left = insert_bst(root.left, v)

  return root


def LCA(root, v1, v2):
  while root and (v1 - root.val) * (v2 - root.val) > 0:
    if v1 < root.val:
      root = root.left
    else:
      root = root.right
  return root

def distance(root, val):
  if not root:
    return 0

  if val > root.val:
    return distance(root.right, val)+1
  elif val < root.val:
    return distance(root.left, val)+1
  else:
    return 0


print(distance_between_nodes([2, 1, 3], 1, 3))
print(distance_between_nodes([2, 1, 4, 3, 5], 1, 5))


