numbers = [1,54,21,5,1,32,53,22]

def maximum(numbers, compare):
    max = numbers[0]
    for number in numbers:
        max = compare(max, number)
    return max

greater = lambda x, y: x if x > y else y

res = maximum(numbers, greater)
print(res)