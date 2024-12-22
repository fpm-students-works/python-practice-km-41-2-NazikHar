def root2(x):
    return x ** (1/2)

def root3(x):
    if x >= 0:
        return x ** (1/3)
    else:
        return -((-x) ** (1/3))