'''
count the number of bits needed to be flipped to convert A to B
'''


def countsetbits(num):
    ctr = 0
    while num:
        num &= (num-1)
        ctr += 1

    return ctr


def countflip(a, b):
    # fact: n ^ n = 0
    # fact: n ^ ~n = 1 -> we use this

    c = a ^ b
    return countsetbits(c)


a, b = list(map(int, input().split()))
print(countflip(a, b))
