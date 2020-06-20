class Node:
    def __init__(self, name):
        self.children = []
        self.name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        # append the root node to array
        array.append(self.name)
        # iterate thru the children of this branch
        for child in self.children:
            child.depthFirstSearch(array)
        return array
