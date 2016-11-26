# --------- #
# Recursion #
# --------- #

# Part 1: Discussion Questions

# Recursion

# In your own words, what is recursion?

# Recursion is when a function calls itself. For example, a set of instructions that
# includes instructions to repeat itself.


# Why is it necessary to have a base case? It's neccessary to have a base case to 
# stop the loop. 
# Graphs

# What is a graph? A graph is a collection of nodes and are vertices, the links are edges.
# How is a graph different from a tree? Graphs have more than one path, trees
# have one path between vertices. Graphs have self-loops and cycles, whereas trees do not have cycles but have directed acyclic graphs.
# Trees have a root node, parent/children relationships, whereas graphs do not. Trees have
# specific rules for connection between nodes through edges wheras graphs do not. Trees have sorting
# and searching tree traversal and binary search applications whereas graphs have graph coloring, job scheduling
# etc.. Trees have n-1 edges and a hierarchical model, whereas graphs do not have edges and have a network model. 



# Give an example of something that would be good to model with a graph. (Biochemistry) Metabolic pathways- glycolysis.

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """

    if my_list:
        print my_list[0]
        print_item(my_list[1:])

# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    print tree.data

    if tree.children:
        for child in tree.children:
            print_all_tree_data(child)

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    if not my_list:
        return 0

    else:
        return list_length(my_list[1:]) + 1



# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    if not tree.children:
        return 1

    counter = 1

    for child in tree.children:
        counter += num_nodes(child)

    return counter

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
