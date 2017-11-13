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

    # def generate_from_pattern_iterative(self, pattern):
    #     child = "l"
    #     current = self.root
    #     for p in pattern:
    #         if p == "(":
    #         if child == "l":
    #             current.l = Node(current)
    #             current = current.l

    def generate_from_pattern(self, pattern):
        self.de_tree(self.root, "l", pattern[1:])

    def de_tree(self, node, child, ptn):
        if not ptn:
            return
        print("%s|%s" % (ptn[0], ''.join(ptn[1:])))
        if ptn[0] == "(":
            if child == "l":
                node.l = Node(node)
                return self.de_tree(node.l, "l", ptn[1:])
            else:
                node.r = Node(node)
                return self.de_tree(node.r, "l", ptn[1:])
        else:
            next_one = (self.next_candidate(node, child))
            return self.de_tree(next_one[0], next_one[1], ptn[1:])

    def next_candidate(self, node, child):
        if child == "l":
            if node.r is None:
                return node, "r"
            sys.exit("we should be here")
        node = node.father
        if node is None:
            sys.exit("too many ')")
        while node.r is not None:
            if node is None:
                sys.exit("too many ')'")
            node = node.father
        return node, "r"

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

    def get_post_order_indexed_by_in_oder_tag(self):
        post_order_list = []
        self._get_post_order_indexed_by_in_oder_tag(self.root, post_order_list)
        return post_order_list

    def _get_post_order_indexed_by_in_oder_tag(self, node, lst):
        if node is not None:
            self._get_post_order_indexed_by_in_oder_tag(node.l, lst)
            lst.append(node.postOrderTag)
            self._get_post_order_indexed_by_in_oder_tag(node.r, lst)

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
