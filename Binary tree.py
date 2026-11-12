r"""Assessment 3.4 - Binary Tree for the last name PLARISAN
The letters are placed level by level (left to right), so the tree is:

            P
          /   \
         L     A
        / \   / \
       R   I S   A
      /
     N
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(name):
    """Build a complete binary tree from a string (level-order insertion)."""
    root = Node(name[0])
    queue = deque([root])
    i = 1
    while i < len(name):
        current = queue.popleft()
        current.left = Node(name[i])
        queue.append(current.left)
        i += 1
        if i < len(name):
            current.right = Node(name[i])
            queue.append(current.right)
            i += 1
    return root


def bfs(root):
    """Breadth-First Search (Level-order) using a queue."""
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(node, out):   # Root -> Left -> Right
    if node:
        out.append(node.data)
        preorder(node.left, out)
        preorder(node.right, out)
    return out


def inorder(node, out):    # Left -> Root -> Right
    if node:
        inorder(node.left, out)
        out.append(node.data)
        inorder(node.right, out)
    return out


def postorder(node, out):  # Left -> Right -> Root
    if node:
        postorder(node.left, out)
        postorder(node.right, out)
        out.append(node.data)
    return out


if __name__ == "__main__":
    root = build_tree("PLARISAN")
    print("BFS (Level-order):", " ".join(bfs(root)))
    print("DFS Preorder     :", " ".join(preorder(root, [])))
    print("DFS Inorder      :", " ".join(inorder(root, [])))
    print("DFS Postorder    :", " ".join(postorder(root, [])))