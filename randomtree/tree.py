from random import choice
import sys


class Node:
    def __init__(self, father):
        self.father = father
        self.l = None
        self.r = None
        self.inOrderTag = None
        self.postOrderTag = None


class Tree:

    def __init__(self):
        self.root = Node(None)
        self.inCount = 1
        self.postCount = 1

    def getRoot(self):
        return self.root

    def generate_from_pattern(self, pattern):
        Tree.de_tree(self.root, pattern)

    @staticmethod
    def de_tree(node, ptn):
        if node is None:
            sys.exit("Invalid pattern, fuck you (none node)")
        if not ptn:
            return
        else:
            print(''.join(ptn))
            if ptn[0] == "(":
                if node.l is None:
                    node.l = Node(node)
                    return Tree.de_tree(node.l, ptn[1:])
                if node.r is None:
                    node.r = Node(node)
                    return Tree.de_tree(node.r, ptn[1:])
                return Tree.de_tree(node.father, ptn)

            elif ptn[0] == ")":
                if node.l is None:
                    if not ptn[1:]:
                        return
                    else:
                        if ptn[1] == ")":
                            if node.r is None:
                                return Tree.de_tree(node.father, ptn[2:])
                            else:
                                return Tree.de_tree(node.father, ptn[2:])
                        elif ptn[1] == "(":
                            node.r = Node(node)
                            return Tree.de_tree(node.r, ptn[2:])
                else:
                    if node.r is None:
                        return Tree.de_tree(node.father, ptn[1:])
                    sys.exit("Invalid pattern, fuck you --- too few ')'")

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
            return self._printTree(self.root, 1)

    def _printTree(self, node, depth):
        if node is not None:
            return "(X \n%sl -> %s\n%sr -> %s)" % ("\t"*depth, self._printTree(node.l, depth+1), "\t"*depth, self._printTree(node.r, depth+1))
        return "none"

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
