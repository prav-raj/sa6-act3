num1 = [3,2,5,7,6,43,4,9]
num2 = [2,7,8,9,4,34,12,6]

res = lambda x: x in num2

result = list(filter(res, num1))
print(result)