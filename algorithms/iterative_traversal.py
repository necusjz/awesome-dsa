def pre_order(root):
    ret = []
    stack, node = [], root
    while stack or node:
        if node:
            ret.append(node.val)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return ret


def in_order(root):
    ret = []
    stack, node = [], root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            ret.append(node.val)
            node = node.right
    return ret


def post_order(root):
    ret = []
    stack, node = [], root
    while stack or node:
        if node:
            ret.append(node.val)
            stack.append(node)
            # move to right first, then reverse its result
            node = node.right
        else:
            node = stack.pop()
            node = node.left
    return ret[::-1]
