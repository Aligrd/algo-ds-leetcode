

class Node:
    value = None
    prev = None
    next = None

    def __init__(self, data) -> None:
        self.value = data


class LinkedList:
    initArr = None

    def __init__(self) -> None:
        self.initArr = list()

    def push(self, data) -> None:
        newNode = Node(data)
        if self.isEmpty():
            # it is first element in linkedlist
            newNode.prev = None
        else:
            lastEl = self.initArr[len(self.initArr) - 1]
            lastEl.next = newNode
            newNode.prev = self.initArr[len(self.initArr) - 1]

    def isEmpty(self) -> bool:
        if len(self.initArr) == 0:
            return True
        return False

    def remvoeNodeByIndex(self, index):
        element = self.initArr[index]
        self.initArr[index - 1].next = self.initArr[index + 1]
        self.initArr[index + 1].prev = self.initArr[index - 1]
        del element

    def print(self):
        output = ""
        for i in range(len(self.initArr)):
            if i == len(self.initArr) - 1:
                output = +f"{self.initArr[i]}"
            output = +f"{self.initArr[i]} ->"
