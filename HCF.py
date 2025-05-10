def hcf(a,b):
    temp = a
    a = b
    b = temp%b
    if b == 0:
        return a
    else:
        return hcf(a,b)


hcf_ = hcf(2,4)
print(hcf_)