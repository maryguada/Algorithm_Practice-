# we first make our class node.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def BFS(self, array):
        # initialize your queue with the root node
        queue = [self]

        # while loop. while there is something in the queue keep running thru this loop
        while len(queue) > 0:

            # assign a value to a current, which is the first thing on your list.
            current = queue.pop(0)

            # for loop thru the children of the current node
            for child in current.children:
                queue.append(child)

        return array
