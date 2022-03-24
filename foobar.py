"""
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, they have several visually-impaired minions.
But Lambda never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard
time navigating her space station. You figure printing out Braille signs will help them, and -- since you'll be
promoting efficiency at the same time -- increase your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3
grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space
station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read"
the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the
following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the
bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle
capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for
spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.
"""

def braille_translation(plaintext :str):
    """ Translating anything to Braille.

    Args:
        plaintext (str): The sentence in human-readable language.

    Returns:
        braille (str): The sentence translated to braille.
    """

    braille_codes = {
        ' ': "000000",
        'a': "100000",
        'b': "110000",
        'c': "100100",
        'd': "100110",
        'e': "100010",
        'f': "110100",
        'g': "110110",
        'h': "110010",
        'i': "010100",
        'j': "010110",
        'k': "101000",
        'l': "111000",
        'm': "101100",
        'n': "101110",
        'o': "101010",
        'p': "111100",
        'q': "111110",
        'r': "111010",
        's': "011100",
        't': "011110",
        'u': "101001",
        'v': "111001",
        'w': "010111",
        'x': "101101",
        'y': "101111",
        'z': "101011",
        '!': "011010",
        'num': "001111",
        'cap': "000001",
    }

    braille = ""
    for i in plaintext:

        if i.isupper():
            braille += braille_codes.get('cap')

        braille += braille_codes.get(i.lower())

    return braille

"""
Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with 
doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar 
panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which 
wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, 
but you'd rather not take down all of the panels at once if you can help it, since they do help power the space 
station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining 
the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output 
of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output 
levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product
would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  
So solution([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output 
level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining 
energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to 
produce the positive output of the multiple of their power values). The final products may be very large, so give the 
solution as a string representation of the number.

"""

def maxProductSubset_naive(xs: list):

    if len(xs) == 1:
        return str(xs[0])

    list_prods = list()
    for i in range(len(xs)):
        prod = xs[i]
        for j in range(len(xs)):
            if j > i:
                if xs[j] == 0 :
                    continue
                prod *= xs[j]

        list_prods.append(prod)

    return str(max(list_prods))


def maxProductSubset(list_numbers: list) :
    if len(list_numbers) == 1 :
        return str(list_numbers[0])

    # Find count of negative numbers, count
    # of zeros, negative number
    # with least absolute value
    # and product of non-zero numbersrequest
    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(len(list_numbers)) :

        # If number is 0, we don't
        # multiply it with product.
        if list_numbers[i] == 0 :
            count_zero += 1
            continue

        # Count negatives and keep
        # track of negative number
        # with least absolute value.
        if list_numbers[i] < 0 :
            count_neg += 1
            max_neg = max(max_neg, list_numbers[i])

        prod = prod * list_numbers[i]

    # If there are all zeros
    if count_zero == len(list_numbers) :
        return str(0)

    # If there are odd number of
    # negative numbers
    if count_neg & 1 :

        # Exceptional case: There is only
        # negative and all other are zeros
        if (count_neg == 1 and count_zero > 0 and
                count_zero + count_neg == len(list_numbers)) :
            return str(0)

        # Otherwise result is product of
        # all non-zeros divided
        # by negative number
        # with least absolute value
        prod = str(int(prod / max_neg))

    return str(prod)

"""
En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. The Commander is a busy lamb, after all! 
Henchmen who identify sources of inefficiency and come up with ways to remove them are generously rewarded. You've 
spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other -- one 
at a time -- before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten 
seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you 
could save several collective hours of employee time per day. But first, you need to show the Commander how bad the 
problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is 
represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an 
employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the 
left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue 
walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number 
of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.
"""
def route_salute(hallway :str):                     # O(n²)

    mapping = dict.fromkeys(range(len(hallway)), 0) # n
    for ind, s in enumerate(hallway):               # n

        if s == "-":
            continue

        if s == ">":
            mapping[ind] = hallway[ind:].count("<") # log n ~ n

        if s == "<":
            mapping[ind] = hallway[:ind].count(">")

    return sum(mapping.values()) # n


def route_salute_2(hallway :str):                   # O(n²)

    counter = 0
    for ind, s in enumerate(hallway):

        if s == ">":
            counter += hallway[ind:].count("<")

    return counter*2