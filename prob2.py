strings = ['prav', 'sam', 'cam', 'gaige', 'luke', 'dylan', 'trent']

res = sorted(strings, key=lambda x: (len(x), x))
print(res)