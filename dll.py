"""
songs will be stored in the form of node in DLL
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    HEAD_NODE = None
    END_NODE = None

    def add_node_at_end(self, new_node: Node) -> Node:
        """
        add a node at the end of DLL.
        if DLL is empty, new_node is the root node
        :param new_node:
        :return:
        """
        if not self.HEAD_NODE:
            self.HEAD_NODE = new_node
            self.END_NODE = new_node
            return new_node

        self.END_NODE.next = new_node
        new_node.prev = self.END_NODE

        self.END_NODE = new_node
        return new_node

    def remove_element(self, node: Node) -> Node:
        """
        remove node from DLL.
        Link node.prev with node.next
        :param node:
        :return:
        """
        if node == self.HEAD_NODE:
            self.HEAD_NODE = self.HEAD_NODE.next
            node.next = None
            if self.HEAD_NODE:
                return node

        if node == self.END_NODE:
            self.END_NODE = node.prev
            node.prev = None
            return node

        if not self.HEAD_NODE:
            self.END_NODE = None
            return node

        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

        return node

    def print_dll(self) -> list:
        node = self.HEAD_NODE
        result = []
        while node != self.END_NODE:
            result.append(node.val)
            node = node.next

        if self.END_NODE:
            result.append(self.END_NODE.val)
        return result
