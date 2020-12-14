#!/usr/bin/env python
# coding: utf-8

# #### .1 Write a Python Program(with class concepts) to find the area of the triangle using the below  formula. 
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
# Function to take the length of the sides of triangle from user should be defined in the parent  class and function to calculate the area should be defined in subclass. 
#  

# In[ ]:


class Length:
    def __init__(self, a, b, c):
        print("Enter the sides")
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())
    
        
        
class Area(Length):
    def area(self, a, b, c):
        s = (self.a+self.b+self.c)/2
       
        areas = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5 
        return (round(areas, 2))
        #print('Area of triangle:', area)

        
obj = Area(a,b,c)
print('area of triangle is',obj.area(a,b,c))
     


# #### 2 Write a function filter_long_words() that takes a list of words and an integer n and returns  the list of words that are longer than n. 

# In[41]:



def filter_long_words(n, lst):
    lst_of_words = []
    for i in range(len(lst)):
        if len(lst[i]) > n:
            lst_of_words.append(lst[i])
    return (lst_of_words)        
            
    
if __name__ == '__main__':


    print("enter n")
    n = int(input())
    print("enter no of words u want to input")
    m = int(input())
    lst = [input() for i in range(m)]  
    final = filter_long_words(n, lst)
    print(final)

    
    
    


# ####  Write a Python program using function concept that maps list of words into a list of integers  representing the lengths of the corresponding words. 
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list. 

# In[46]:


def list_of_integer(lst):
    num = []
    for i in range(len(lst)):
        num.append(len(lst[i]))
    return num

 
    
if __name__ == '__main__':    
    print('enter no of words')
    m = int(input())
    print("enter the words")
    lst = [input() for i in range(m)] 
    n = list_of_integer(lst)
    print(n)


# #### .2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if  it is a vowel, False otherwise. 

# In[55]:


def vowels(m):
    if len(m)>1:
         return("character should be of length 1")
          
        
    if m in vowel:
        return True
    else:
        return False
    
    
    
    
if __name__ == '__main__':
    vowel = ['a','e','i','o','u']
    print('enter a character')
    m = input()
        
    final = vowels(m)
    print(final)


# In[ ]:





# In[ ]:




