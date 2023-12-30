from src.circular_queue import CircularQueue


def test_circular_queue():
    queue = CircularQueue(3)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    assert queue.rear() == 3
    assert queue.is_full() is True

    queue.dequeue()
    queue.enqueue(4)

    assert queue.rear() == 4
