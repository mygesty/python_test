# coding:utf-8

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop(0)
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                elif cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)

    def breadth(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)

