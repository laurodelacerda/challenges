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


'''
    Write a function:

    def solution(A)

    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.

    Given A = [−1, −3], the function should return 1.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def smallest_positive(A: list):
    
    biggest = -1
    for i in A:
        if i > 0:
            biggest = max(biggest, i)

    if biggest <= 0:
        return 1  

    for i in range(1, 100000):
        if i not in A:
            return i


''''''
def sum_multiple_4(A: list): 

    multiple_4 = list()
    for i in A:
        if i % 4 == 0:
            multiple_4.append(i)

    return sum(multiple_4)

'''
    There are N coins, each showing either heads or tails. We would like all the coins to form a sequence of 
    alternating heads and tails. What is the minimum number of coins that must be reversed to achieve this?
    
    Write a function:
    def solution (A)

    that, given an array A consisting of N integers representing the coins, returns the minimum number of coins that 
    must be reversed. Consecutive elements of array A represent consecutive coins and contain either a 0 (heads) or a 
    1 (tails).

    Examples:
    1. Given array A = [1, 0, 1, 0, 1, 1], the function should return 1. After reversing the sixth coin, we achieve an 
    alternating sequence of coins [1, 0, 1, 0, 1, 0]. 
    2. Given array A = [1, 1, 0, 1, 1], the function should return 2. After reversing the first and fifth coins, we 
    achieve an alternating sequence [0, 1, 0, 1, 0]. 
    3. Given array A = [0, 1, 0], the function should return O. The sequence of coins is already alternating. 
    4. Given array A = [0, 1, 1, 0], the function should return 2. We can reverse the first and second coins to get the 
    sequence: [1, 0, 1, 0].
    
    Assume that:
        • N is an integer within the range [1..100]; 
        • each element of array A is an integer that can have one of the following values: 0, 1.

    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''

def flip_heads_or_tails(A: list):

    return min(sum(n ==  i % 2      for i, n in enumerate(A)),
               sum(n == (i + 1) % 2 for i, n in enumerate(A)))



