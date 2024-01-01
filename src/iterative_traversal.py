def prev_order(root):
    sequence = []

    stack, node = [], root
    while stack or node:
        if node:
            sequence.append(node.val)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right

    return sequence


def in_order(root):
    sequence = []

    stack, node = [], root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            sequence.append(node.val)
            node = node.right

    return sequence


def post_order(root):
    sequence = []

    stack, node = [], root
    while stack or node:
        if node:
            sequence.append(node.val)
            stack.append(node)
            node = node.right  # right first, then reverse
        else:
            node = stack.pop()
            node = node.left

    return sequence[::-1]
