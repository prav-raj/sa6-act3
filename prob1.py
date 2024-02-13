num = [str(43)]

res = list(map(lambda x: sum(int(y) for y in str(x)), num))
print(res)