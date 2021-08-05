class Node(object):

    def __init__(self, data=None, prox=None):
        self.data = data
        self.prox = prox

    def __str__(self):
        return str(self.data)


v3 = Node("Bananas")
v2 = Node("Peras", v3)
v1 = Node("Manzanas", v2)

print(v1, v2, v3)


def view_list(node):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras el node no es None
    while node:
        # imprime el node
        print(node)

        # ahora node apunta a node.prox
        node = node.prox


view_list(v1)
