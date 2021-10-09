#!/usr/bin/env python
# coding: utf-8

# In[22]:


import random

def guess_the_number(x):
    
    random_number=random.randint(1,x)   #this will select a random number form range the of 1 to x
    guess=0
    attempt=0
    
    i=0 #used for 1st statement
    
    while random_number!=guess:
        if i==0:
            guess=int(input(f'Guess a random number from 1 to {x} :'))
        else:
            guess=int(input("Guess again :"))
        
        if guess<random_number:      
            print("Your guessed number is smaller than a random number")
        
        elif guess>random_number:
            print("Your guessed number is larger than a random number")
        
        i=1
        attempt+=1
    
    if attempt==1:
        print(f"WoW, Congratulations!! You have guessed the random number {random_number} in your 1st attempt!!")
    
    elif attempt>1 and attempt<=3:
        print(f"Congrats!! You have guessed the random number {random_number} in just {attempt} attempts.")
    
    else:
        print(f"You have guessed the random number {random_number} in {attempt} attempts, better luck next time.")
    
    
    
select_range= int(input("Enter a range for a random number: "))

guess_the_number(select_range)
   


# In[ ]:




