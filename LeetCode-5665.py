# Restore array from adjacant pairs

adjArr = [[2, 1], [3, 4], [3, 2]]  # [1,2 ,3,4]
adjArr2 = [[4, -2], [1, 4], [-3, 1]]  # [1,2 ,3,4]

#!      sort subarrays      => flatten the arr => make a set from arr => result
#! [[1, 2], [3, 4], [2, 3]] => [1,2,3,4,2,3] => set([1,2,3,4,2,3]) => [1,2,3,4]


#! we need to sort every pair in 2D arr then we need to flatten the arr
def Restore(adjacant_pair: list[int]):
    init_arr = []
    map = {}
    dfs_entry_point = 0
    for pair in adjacant_pair:
        map[pair[1]] = pair[0]
        map[pair[0]] = pair[1]
    for i in map.keys():
        init_arr.append(i)
    for i in map.values():
        init_arr.append(i)
    entry_point = find_unique_elemets(init_arr)


# print(Restore(adjArr))


def dfs(graph: list[list]):
    visited = []
    stack = []
    for elm in list:
        for vertex in list:
            vertex ! 
        

def find_unique_elemets(l: list):
    collectr = []
    unique = l[0]
    for i in range(1, len(l)):
        if l[i] in collectr:
            unique = l[i]
    return unique


# print(find_unique_elemets(Restore(adjArr2)))
