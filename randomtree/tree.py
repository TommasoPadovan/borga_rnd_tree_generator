from random import choice


class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.inOrderTag = None
        self.postOrderTag = None


class Tree:

    def __init__(self):
        self.root = Node()
        self.frontier = [self.root, self.root]
        self.nodeCount = 1
        self.inCount = 1
        self.postCount = 1

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
        self.frontier.remove(candidate)

        # add the node -> the new node is obviously a leaf -> so it is in the frontier
        if which == "l":
            candidate.l = Node()
            self.frontier.append(candidate.l)
            self.frontier.append(candidate.l)
        elif which == "r":
            candidate.r = Node()
            self.frontier.append(candidate.r)
            self.frontier.append(candidate.r)

        # update the node count
        self.nodeCount += 1

    def in_order_visit(self):
        self.visit_in(self.root)

    def visit_in(self, node):
        if node is None:
            return
        self.visit_in(node.l)
        node.inOrderTag = self.inCount
        self.inCount += 1
        self.visit_in(node.r)

    def post_order_visit(self):
        self.visit_post(self.root)

    def visit_post(self, node):
        if node is None:
            return
        self.visit_post(node.l)
        self.visit_post(node.r)
        node.postOrderTag = self.postCount
        self.postCount += 1

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print ("(%s, %s)" % (node.inOrderTag, node.postOrderTag))
            self._printTree(node.r)

    def output_csv(self):
        if self.root is not None:
            f = open("culo.csv", "w+")
            f.write("in_oder, post_order\n")
            self._output_csv(self.root, f)
            f.close()

    def _output_csv(self, node, f):
        if node is not None:
            self._output_csv(node.l, f)
            f.write("%s, %s\n" % (node.inOrderTag, node.postOrderTag))
            self._output_csv(node.r, f)

    @staticmethod
    def output_csv_multiple(trees):
        f = open("culo.csv", "w+")
        i = 0
        for tree in trees:
            root = tree.getRoot()
            i += 1
            f.write("in %s, " % i)
            Tree._output_csv_line_in(root, f)
            f.write("\n")
            f.write("out %s, " % i)
            Tree._output_csv_line_post(root, f)
            f.write("\n,\n")

    @staticmethod
    def _output_csv_line_in(node, f):
        if node is not None:
            Tree._output_csv_line_in(node.l, f)
            f.write("%s, " % node.inOrderTag)
            Tree._output_csv_line_in(node.r, f)

    @staticmethod
    def _output_csv_line_post(node, f):
        if node is not None:
            Tree._output_csv_line_post(node.l, f)
            f.write("%s, " % node.postOrderTag)
            Tree._output_csv_line_post(node.r, f)

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
