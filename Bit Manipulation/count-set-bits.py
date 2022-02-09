'''
Given a positive integer N, print count of set bits in it.
'''


def count1(num):
    # pythonic way
    # bin(integer) -> '0b[binary rep]'
    # bin(8) -> '0b1000'

    return bin(num).count('1')


def count2(num):
    # optimal way
    # brian kerninghan's algo
    # fact: n & n-1 will unset the 'rightmost' set bit
    # for each time you do this action, you encounter a set bit

    ctr = 0
    while num:
        num &= (num-1)
        ctr += 1

    return ctr


N = int(input())
print(count1(N), count2(N))
