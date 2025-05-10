def hcf(a,b):
    temp = a # temp = 2   temp = 4
    a = b # a = 4         a = 2
    b = temp % b  # b = 2 % 4 = 2     b = 4 % 2 = 0 so now return the value of a
    if b == 0:
        return a
    else:
        return hcf(a,b)


hcf_ = hcf(2,4)
print(hcf_)