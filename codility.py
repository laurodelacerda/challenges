# -*- coding: utf-8 -*-
"""
author: Lauro de Lacerda
e-mail: lauro.lacerda@gmail.com

Challenges Codility
"""


'''
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at 
    both ends in the binary representation of N.
    
    For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has 
    binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 
    has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 
    1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

    Write a function:
        def solution(N)

    that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N 
    doesn't contain a binary gap.
    
    For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its 
    longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation 
    '100000' and thus no binary gaps.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..2,147,483,647].
'''
def binary_gap(N :int) -> int:
    '''
        Args:
            N (int): A positive N
    '''

    binary = "{0:b}".format(N)
    binary_gap = 0
    max_gap    = 0

    flag_start = False

    print(binary)

    for item in binary:

        if item == '0':
            
            if flag_start:
                binary_gap += 1

        if item == '1':

            if flag_start:
                max_gap = max(max_gap, binary_gap)
                binary_gap = 0
            else:
                flag_start = True

    return max_gap

'''
    A positive integer N is given. The goal is to find the highest power of 2 that divides N. In other words, we have to 
    find the maximum K for which N modulo 2^K is 0.

    For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

    Write a function:

        def solution(N)

    that, given a positive integer N, returns the highest power of 2 that divides N.

    For example, given integer N = 24, the function should return 3, as explained above.

    Assume that:

    N is an integer within the range [1..1,000,000,000].
    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''
def parity_degree(N :int) -> int:
    '''
        Args:
            N (int): A positive N
    '''

    max_power = 0
    for k in range(0, N):
        if N % 2**k == 0:
            max_power = max(max_power, k)

    return max_power