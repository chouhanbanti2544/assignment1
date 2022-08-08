#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 

# Q.1            
# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# In[2]:


def fib(n):
    a = 1
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l
print(fib(10))


# Q.2 Write a Python program that accepts a word from the user and reverse it.
# Sample Test Case
# Input : Hello 
# output: olleH

# In[3]:


h = "Hello"
l=" "
for i in h:
    l=i+l
print(l)


# Q.3 Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# In[6]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
l=[]

for i in range(len(numbers)):
    if numbers[i]%2==0:
        l.append(numbers[i])


print("even number",l)
print("number of even numbers:",len(l))


odd=[]
for j in numbers:
    if j%2!=0:
        odd.append(j)

print("odd number:",odd)      
print("number of odd numbers:",len(odd))


# In[ ]:




