def filter(nums: list[int]):
    positive = []
    negative = []

    for i in nums:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    return (positive, negative)


data = [-1, -2, 1, 2, -3, 1, 34]

r = filter(data)

print(r)
