from random import choice


class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.inOrderTag = None
        self.postOrderTag = None


class Tree:
    inCount = 1
    postCount = 1

    def __init__(self):
        self.root = Node()
        self.frontier = [self.root]
        self.nodeCount = 1

    def getRoot(self):
        return self.root

    def rnd_add(self):
        # choose a random node in the frontier
        candidate = choice(self.frontier)

        # check which of his "child-slots" is free
        possibleChildren = []
        if candidate.l is None:
            possibleChildren.append("l")
        if candidate.r is None:
            possibleChildren.append("r")

        # choose one among the possible children
        which = choice(possibleChildren)
        possibleChildren.remove(which)

        # if it was the last child free -> the father node is "complete" (has 2 children) -> remove if from frontier
        if not possibleChildren:
            self.frontier.remove(candidate)

        # add the node -> the new node is obviously a leaf -> so it is in the frontier
        if which == "l":
            candidate.l = Node()
            self.frontier.append(candidate.l)
        elif which == "r":
            candidate.r = Node()
            self.frontier.append(candidate.r)

        # update the node count
        self.nodeCount += 1

    def in_order_visit(self):
        Tree.visit_in(self.root)

    @staticmethod
    def visit_in(node):
        if node is None:
            return
        Tree.visit_in(node.l)
        node.inOrderTag = Tree.inCount
        Tree.inCount += 1
        Tree.visit_in(node.r)

    def post_order_visit(self):
        Tree.visit_post(self.root)

    @staticmethod
    def visit_post(node):
        if node is None:
            return
        Tree.visit_post(node.l)
        Tree.visit_post(node.r)
        node.postOrderTag = Tree.postCount
        Tree.postCount += 1

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print ("(%s, %s), " % (node.inOrderTag, node.postOrderTag))
            self._printTree(node.r)



#     3
# 0     4
#   2      8


# tree = Tree()
# tree.add(3)
# tree.add(4)
# tree.add(0)
# tree.add(8)
# tree.add(2)
# tree.printTree()
# print (tree.find(3)).v
# print tree.find(10)
# tree.deleteTree()
# tree.printTree()
