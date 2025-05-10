def hcf(a,b):
    while b!=0:
        t = a
        a = b
        b = t % b
    return a
def lcm(a,b):
    return (a*b)//hcf(a,b)
print(hcf(12,4))
print(lcm(12,4))