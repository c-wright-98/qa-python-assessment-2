# -------------------------------------------------------------------------------------------------------------------------------------------------

# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:
#
# 	<QUESTION>
#
# 	<EXAMPLES>
#
# 	<HINT>

# You are allowed access to the internet for this assessment, but remember you could use the DOCUMENTATION that comes bundled with your Python installation.
# Every command has help documentation. To read it:
# 	1. Access Python from your CLI
# 	2. Type help(<command>) and hit enter, where <command> is the command you want help with. For example: help(str)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?

def one(string):
    new_string = ''
    for i in string:
        new_string += i*3
    return new_string

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 2>

    # Write a function which returns the boolean True if the input is only divisible by one and itself.

    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(number):
    if number > 1:
        for i in range(2,int(number/2)+1):
            if number % i == 0:
                return False
        else:
            return True


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?


def three(a):
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a,a))
    n3 = int("%s%s%s" % (a,a,a))
    n4 = int("%s%s%s%s" % (a,a,a,a))
    return (n1+n2+n3+n4)


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.

    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee"
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?


def four(string1, string2):
    string = ""
    for char1, char2 in zip(string1, string2):
        # the zip function creates an iterator that will aggregate elements from two or more iterables.
        string += char1 + char2
    return string

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.

import random

def five():
    ls = []
    while len(ls) < 5:
        num = random.randint(100, 200)
        if num % 2 == 0:
            ls.append(num)
    return ls

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not.

    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.


def six(string):
    if string.endswith("py") or string.endswith("pY") or string.endswith("PY") or string.endswith("Py"):
        return True
    return False

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large.

    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large.

    # Do not assume the ints will come to you in a reasonable order.

    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)


def seven(a, b, c):
    nums = [a,b,c]
    nums.sort()
    return nums[1] - nums[0] == nums[2] - nums[1]

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(string,  a):
    middle_index = len(string) // 2
    remove = a // 2

    if a % 2 == 0: # even integer
        result = string[:middle_index - remove] + string[middle_index + remove:]
    else:# odd integer
        result = string[:middle_index - remove] + string[middle_index + remove+1:]
    return result

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
    # Count the individual characters in the string
    count1 = {}
    count2 = {}

    for i in string1:
        count1[i] = count1.get(i,0) +1
        #increments the count by 1 for the letters, if it does not exist it adds it with 0 and then adds 1
    for i in string2:
        count2[i] = count2.get(i,0) +1

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, x,y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(x, y):
    #an array is lists within a list, allowing you to make matrix's and arrays
    if x > 0 and y > 0:
        array = [[i*j for j in range(x)]for i in range(y)]
    else:
        array = []
    return array

# -------------------------------------------------------------------------------------------------------------------------------------------------
