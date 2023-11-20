# solve it with 2pointer left and right
# dont make extra memory alocation and manipulate the same list(dont make another list to store unique element)


def solve(list: list[int]) -> list[int]:
    l = 1
    for r in range(1, len(list)):
        if list[r] != list[r - 1]:
            list[l] = list[r]
            l += 1
    for i in range(l, len(list)):
        list[i] = None
        
    return list


list1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
list2 = solve(list1)
print(list2)
