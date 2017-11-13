from tree import Tree
from parenthesis import tryAndFix
from permutations import associated_permutation

# edit this to change the number of nodes
NODE_NUMBER = 20

# edit this to change the number of tries of your experiment
TRIES = 10


K = 3

trees = [None] * TRIES


def swag(lst):
    s = ''
    for i in lst:
        s += str(i)
        s += "\t"
    return s


tree = Tree()

tree.generate_from_pattern(tryAndFix(NODE_NUMBER))

tree.in_order_visit()

tree.post_order_visit()

print(tree.printTree())

tree.output_csv()

permutations = tree.get_post_order_indexed_by_in_oder_tag()

print(swag(permutations))


d = {}
for offset in range(0, len(permutations)-K+1):
    ass_perm = associated_permutation(permutations[0+offset:K+offset])
    if ass_perm in d:
        d[ass_perm] += 1
    else:
        d[ass_perm] = 1
    print ("%s%s" % ("\t"*offset, swag(ass_perm)))

for key in d:
    print ("%s -> %s" % (key, d[key]))


