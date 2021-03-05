b = {2: 5,
     3: 1}
def inverser(x):
    return 1.0 / x
print(b.keys())
print(max(b.keys(), key=inverser))