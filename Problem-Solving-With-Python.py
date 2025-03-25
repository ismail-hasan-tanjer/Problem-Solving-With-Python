'''🔥 Programming Problem Solving Questions and Solutions
1️⃣ Problem: FizzBuzz
Description: For numbers from 1 to n—

If the number is divisible by 3, then print "Fizz".
If the number is divisible by 5, then print "Buzz".
If it is divisible by both 3 and 5, then print "FizzBuzz".
Otherwise, print the number itself.'''

#solutions

#code 

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# test run 
fizzbuzz(15)

'''
2️⃣ Problem: Palindrome Check
Description: Given a string. Check whether it is a palindrome (i.e., whether it is the same when reversed).

✅ Python code: 
'''

    
def is_palindrome(s):
    return s == s[::-1]

# Test 
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

'''
3️⃣ Problem: Fibonacci Series
Description: Create a Fibonacci series where each number is the sum of the previous two numbers. Starting from 0, 1.

✅ Python code:
'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Test Run
fibonacci(10)

'''Problem: Prime Number Check
Description: Check if a number is prime (i.e., not divisible by any number other than 1 and itself).

✅ Python code:
'''
    
def is_prime(n):
    
    return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test Run 
print(is_prime(7))  # True
print(is_prime(10))  # False

# Problem: Reverse an Integer
# Description: Given a number as input, return its inverted form.

# ✅ Python code:

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    rev_num = int(str(abs(n))[::-1])
    return sign * rev_num

# Test
print(reverse_integer(123))  # 321
print(reverse_integer(-456))  # -654

# New Some Problem 
"""
    1️ Finding the sum of digits from a number
👉 Problem: Given a number, your task is to find the sum of each of its digits.

🔹 Input: 12345
🔹 Output: 15 (1 + 2 + 3 + 4 + 5 = 15)    
"""

#code 

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# example
print(sum_of_digits(12345))  # Output: 15
print(sum_of_digits(9876))   # Output: 30


"""
    
    2️⃣ Check if the number is an Armstrong number
👉 Problem: Given a number, we need to find out if it is an Armstrong number.

🔹 Input: 153
🔹 Output: True (1³ + 5³ + 3³ = 153)

    """
    
def is_armstrong(n):
        num_str = str (n)
        power = len(num_str)
        return n == sum(int(digit) ** power for digit is num_str)
    
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))

"""
3️⃣ Counting vowels in a string
👉 Problem: Given a string, your task is to find how many vowels (a, e, i, o, u) are in it.

🔹 Input: "hello world"
🔹 Output: 3 (e, o, o)
"""

#counting vowels code 

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# example 
print(count_vowels("hello world"))  # Output: 3
print(count_vowels("Python Programming")) # Output: 5

    """
    4️⃣ Finding Factors of Numbers
👉 Problem: Given a number, you need to find all its factors.

🔹 Input: 12
🔹 Output: [1, 2, 3, 4, 6, 12]
    """

#code 
def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# used example 
print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(find_factors(15))  # Output: [1, 3, 5, 15]

    """
    5️⃣ Finding the LCM of two numbers
👉 Problem: Given two numbers, find the Least Common Multiple (LCM) of them.

🔹 Input: 4, 6
🔹 Output: 12
    """
    
    import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# used example 
print(lcm(4, 6))   # Output: 12
print(lcm(10, 15)) # Output: 30


    """
    6️⃣ Finding the average of all the elements of an array
👉 Problem: Given a list, we need to find the average of all the numbers in it.

🔹 Input: [10, 20, 30, 40, 50]
🔹 Output: 30.0
    """
#code  
    def average(lst):
    return sum(lst) / len(lst) if lst else 0

# example 
print(average([10, 20, 30, 40, 50]))  # Output: 30.0
print(average([5, 15, 25]))  # Output: 15.0

    """
    7️⃣ Check if two strings are anagrams
👉 Problem: Given two strings, we need to find out if they are anagrams.

🔹 Input: "listen", "silent"
🔹 Output: True
    """
    
    def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Example 
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False

"""
8️⃣ Finding the unique numbers of all elements in a list
👉 Problem: Given a list, you need to find its unique numbers.

🔹 Input: [1, 2, 2, 3, 4, 4, 5]
🔹 Output: [1, 2, 3, 4, 5]      
"""

#coding 

def unique_elements(lst):
    return list(set(lst))

# example 
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique_elements([10, 20, 10, 30]))  # Output: [10, 20, 30]


1️⃣ Reverse each digit of a number
👉 Problem: Given a number, its digits need to be reversed.

🔹 Input: 12345
🔹 Output: 54321

#coding 

def reverse_digits(n):
    return int(str(n)[::-1])

# example 
print(reverse_digits(12345))  # Output: 54321
print(reverse_digits(9876))   # Output: 6789


Finding the Fibonacci series of numbers
👉 Problem: Given a number, find its first N Fibonacci numbers.

🔹 Input: 5
🔹 Output: [0, 1, 1, 2, 3]

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

#example 
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(8))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]


Checking if a digit of a number is a palindrome
👉 Problem: Given a number, we need to check if it is a palindrome.

🔹 Input: 121
🔹 Output: True

#coding 

def is_palindrome(n):
    return str(n) == str(n)[::-1]

#example 
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False


Counting the number of each character in a string
👉 Problem: Given a string, we need to find how many times each character appears in it.

🔹 Input: "banana"
🔹 Output: {'b': 1, 'a': 3, 'n': 2}

from collections import Counter

def char_count(s):
    return dict(Counter(s))

# example 
print(char_count("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}
print(char_count("hello"))   # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


Count the words in a string
👉 Problem: Given a sentence, find how many words it contains.

🔹 Input: "Python is a great language"
🔹 Output: 5