from random import getrandbits


class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class SkipList:
    def __init__(self):
        # dummy head
        self.head = Node()

    def search(self, target):
        node = self.head
        while node:
            # move to right in current level
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            # move to next level
            node = node.down
        return False

    def insert(self, num):
        nodes = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down
        insert, down = True, None
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = (getrandbits(1) == 0)
        if insert:
            # create new level with dummy head
            self.head = Node(-1, None, self.head)

    def delete(self, num):
        node, found = self.head, False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                # delete by skipping
                node.right = node.right.right
                found = True
            node = node.down
        return found
