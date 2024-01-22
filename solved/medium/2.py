from typing import Optional


def solution(l1: list[int], l2: list[int]) -> list[int]:
    n1 = 0
    for i, n in enumerate(l1):
        n1 += n * (10**i)

    n2 = 0
    for i, n in enumerate(l2):
        n2 += n * (10**i)

    total = n1 + n2
    ltotal = [int(n) for n in str(total)]

    return ltotal


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    rl1 = []
    while l1 is not None:
        rl1.append(l1.val)
        l1 = l1.next

    rl2 = []
    while l2 is not None:
        rl2.append(l2.val)
        l2 = l2.next

    n1 = 0
    for i, n in enumerate(rl1):
        n1 += n * (10**i)

    n2 = 0
    for i, n in enumerate(rl2):
        n2 += n * (10**i)

    total = n1 + n2
    ltotal = [int(n) for n in str(total)]

    current_node = None
    for value in ltotal:
        current_node = ListNode(val=value, next=current_node)

    return current_node


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    r = solution(l1, l2)
    print(r.val)
