from collections import Counter, deque
from functools import reduce
import heapq
import random


class MonoliticStack:
    def __init__(self) -> None:
        pass


def StringTwoNumber(string, encodeProtocol):
    match encodeProtocol:
        case "utf-8":
            byteArr = bytes(string, "utf-8")
            return int.from_bytes(byteArr)

        case "ascii":
            byteArr = bytes(string, "ascii")
            return int.from_bytes(byteArr)


# print(ord("a"))
# def makeMonolotoc(arrList: list, direction: str) -> list:
#     newlist = []

#     if direction == "increasing":
#         for n in range(len(arrList)):
#             currentElement = arrList[n]
#             if arrList[n + 1] >= currentElement:
#                 newlist.append(arrList[n + 1])

#     elif direction == "decreasing":
#         for n in range(len(arrList)):
#             currentElement = arrList[n]
#             if arrList[n] <= currentElement:
#                 newlist.append(arrList[n + 1])
#     return newlist


# myList = [1, 4, 5, 3, 12, 10]

# mList = makeMonolotoc(myList , "increasing")

# print(mList)

# abcab => abc - bca - cab

# find the unique then find the one witch corerespond to lexicographical order


def removeDuplicate(s: str):
    result: str = ""
    for i in s:
        if i in result:
            continue
        result += i
    return result

    # there should be something to keep track of frequency of each letter -> we shouldnt remove a non appearing letter
    # there should be something to keep track of visitation of letter -> we need to know if
    # we need to keep track of lexical graphic order in stack between 2 subsequent letter


import io
import http

def removeDuplicateLetters(s: str) -> str:
    stack = []
    freqCounter = Counter(s)
    seenList = set()
    for char in s:
        freqCounter[char] -= 1
        if char in stack:
            continue
        while stack and char < stack[-1] and freqCounter[stack[-1]] > 0:
            removed = stack.pop()
            seenList.remove(removed)

        stack.append(char)
        seenList.add(char)
    return "".join(stack)



myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

freq = dict()
string = "bcabc"

for i in range(len(string)):
    freq[string[i]] = i
print(freq)

# pq = heapq.heapify(myList)


def randomList(min, max, length):
    rndList = [0 for i in range(length)]
    for i in range(length):
        rndNumber = random.choice(range(min, max))
        rndList[i] = rndNumber
    return rndList


dataList = randomList(10, 50, 10)

# print(dataList)
# print(sorted(dataList))
#! incremental list of int
list(range(10))
