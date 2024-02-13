numbers = [2, 3, 4, 5, 6]
n = 3

res = lambda x: x ** n

result = list(map(res, numbers))
print(result)