#1
def myfunc(grams):
    return grams/28.3495231
grams = float(input("Enter the number of grams: "))
ounces = myfunc(grams)
print(ounces)

#2
def myfunc(Fahrenheit):
    return (5/9)*(Fahrenheit-32)
Fahrenheit = float(input("Enter the Fahrenheit temperature"))
Centigrade = myfunc(Fahrenheit)
print(f"{Fahrenheit} F = {Centigrade:.2f} C")

#3
"""
numheads = heads
numlegs = legs
x = chickens
y = rabbits
{x + y = heads
2x + 4y = legs}
{x = heads - y
2(heads - y) + 4y = legs}
heads * 2 - 2y + 4y = legs
heads * 2 + 2y = legs
2y = legs - heads * 2
y = (legs - heads * 2) / 2
"""

def solve(numheads, numlegs):
    y = (numlegs - numheads * 2) // 2 
    x = numheads - y
    return x, y

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")

#4
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:  
            return False
    return True

def filter_prime(numbers):
    filtered_list = []
    for num in numbers:
        if is_prime(num):  
            filtered_list.append(num)  
    return filtered_list 

numbers = [5, 2, 31, 12, 11, 23, 19, 45]
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#5
from itertools import permutations
# permutations create all possible variants
def all_permutations():
    user_input = input("Enter a string: ")
    perm_list = permutations(user_input)
# itertools.permutations returns an iterator yielding tuples, so we join each tuple to form strings
    for perm in perm_list:
        print("".join(perm))

all_permutations()

#6
def myfunc(sentence):
    words = sentence.split() 
    reversed_sentence = " ".join(reversed(words))  
    return reversed_sentence

user_input = input("Enter a sentence: ") 
print(myfunc(user_input)) 

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3: 
            return True  
    return False  

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7] 
    
    for num in nums:
        if num == code[0]:  
            code.pop(0)  
        if not code:  
            return True  
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

#9
import math  
def volume(radius):
    return (4/3) * math.pi * (radius ** 3)

r = float(input("Enter the radius of the sphere: ")) 
print("Volume of the sphere:", volume(r))  

#10
def unique_elements(lst):
    unique_list = [] 
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)
    return unique_list  

user_input = input("Enter numbers: ") 
numbers = list(map(int, user_input.split())) 
print("Unique numbers:", unique_elements(numbers))

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1] 
    
user_input = input("Enter a word or phrase: ")  
if is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not a palindrome")

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num) 
histogram([4, 9, 7])

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)  
    attempts = 0  

    while True:
        try:
            print("\nTake a guess.")
            guess = int(input()) 
            attempts += 1

            if guess < number_to_guess:
                print("\nYour guess is too low.")
            elif guess > number_to_guess:
                print("\nYour guess is too high.")
            else:
                print(f"\nGood job, {name}! You guessed my number in {attempts} guesses!")
                break 
        except ValueError:
            print("\nPlease enter a valid number between 1 and 20.")

guess_the_number()
