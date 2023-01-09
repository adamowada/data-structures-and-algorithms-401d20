class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree implementation
    """
    def __init__(self):
        self.root = None

    def pre_order(self, root=None, nodes=None):
        """
        Return a list of nodes in BT, in pre-order
        """
        if nodes is None:
            nodes = []

        if root is None:
            root = self.root

        # root
        nodes.append(root.val)

        # left
        if root.left:
            self.pre_order(root.left, nodes)

        # right
        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def post_order(self, root=None, nodes=None):
        """
        Return a list of nodes in BT, in post-order
        """
        if nodes is None:
            nodes = []

        if root is None:
            root = self.root

        # left
        if root.left:
            self.post_order(root.left, nodes)

        # right
        if root.right:
            self.post_order(root.right, nodes)

        # root
        nodes.append(root.val)

        return nodes

    def in_order(self, root=None, nodes=None):
        """
        Return a list of nodes in BT, in in-order
        """
        if nodes is None:
            nodes = []

        if root is None:
            root = self.root

        # left
        if root.left:
            self.in_order(root.left, nodes)

        # root
        nodes.append(root.val)

        # right
        if root.right:
            self.in_order(root.right, nodes)

        return nodes



