from src.design_patterns.iterator import ListNode, LinkedList


def test_iterator():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    for i, node in enumerate(LinkedList(head)):
        assert node == i + 1
