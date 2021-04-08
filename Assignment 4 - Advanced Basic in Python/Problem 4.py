# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:14:20 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Find out palindromic prime number between a range.
def one_digit(number):
    return (number>=0 and number<10)
def is_palindrome_utility(number,dupNum):
    if(one_digit(number)):
        return (number==(dupNum)%10)
    if(not is_palindrome_utility(int(number/10),dupNum)):
        return False
    dupNum=int(dupNum/10)
    return (number%10==(dupNum)%10)
def is_palindrome(number):
    if(number<0):
        number=-number
    dupNum=number
    return is_palindrome_utility(number,dupNum)
def print_palindrome_prime(n):
    prime=[True]*(n+1)
    p=2
    while(p*p<=n):
        if(prime[p]):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n+1):
        if(prime[p] and is_palindrome(p)):
            print(p,end=" ")

n=int(input("Enter the higher range: "))
print("Plaindromic prime in your range: ")
print(print_palindrome_prime(n))

#Input: Enter the higher range:10
#Output: 2 3 5 7 None