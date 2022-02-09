'''
Given an array A containing 2*N+2 positive numbers
2*N numbers exist in pairs
'''


def find1(arr):
    # using maps/dictionaries
    # fact: maps in python cannot be edited during traversal

    mp = {}
    for x in arr:
        if x not in mp:
            mp[x] = 1
        else:
            mp[x] += 1

    return [x for x in mp if mp[x] == 1]


def find2(arr):
    # using sets
    # add every element that does not exist in set
    # delete every element that exists in set
    # sets can be modified during traversal

    s = set()
    for x in arr:
        if x not in s:
            s.add(x)
        else:
            s.remove(x)

    return list(s)


def find3(arr):
    # using bit manipulation
    # fact: n & ~(n-1) gives rightmost set bit mask
    # bit mask helps to indentify that particular bit in any no.
    # fact: n ^ n = 0

    x, y = 0, 0

    xxory = 0
    for a in arr:
        xxory = xxory ^ a  # this will cancel out all repeating nos.

    # since all repeating elements have cancelled out
    # xxory will literally be xor of 2 non-repeating elements

    # now we create rightmost set bit mask for xxory
    # based on it we divide the array into 2 parts
    # 1 with rightmost set bit matching any of x and y and vice-versa

    rbms = xxory & -(xxory-1)

    for a in arr:
        # check if rbms matches our element
        if rbms & a:
            x = x ^ a
        else:
            y = y ^ a

    return [x, y]


arr = list(map(int, input().split()))
print(find1(arr), find2(arr), find3(arr))
