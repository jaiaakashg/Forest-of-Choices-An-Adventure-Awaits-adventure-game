#!/usr/bin/env python
# coding: utf-8

# In[1]:


def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths in front of you.")
    print("1. Take the left path")
    print("2. Take the right path")
    
    choice = input("Which path do you choose? (1 or 2): ")
    
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_adventure()

def left_path():
    print("You take the left path and find a peaceful clearing with a small pond.")
    print("You can either rest by the pond or continue exploring.")
    print("1. Rest by the pond")
    print("2. Continue exploring")
    
    choice = input("What do you want to do? (1 or 2): ")
    
    if choice == '1':
        print("You rest by the pond and regain your strength. You win!")
    elif choice == '2':
        print("You continue exploring and find a hidden treasure chest. You win!")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path()

def right_path():
    print("You take the right path and encounter a wild animal.")
    print("You can either try to fight the animal or run away.")
    print("1. Fight the animal")
    print("2. Run away")
    
    choice = input("What do you want to do? (1 or 2): ")
    
    if choice == '1':
        print("You fight the animal and manage to scare it away. You win!")
    elif choice == '2':
        print("You run away and find yourself back at the start. Try again.")
        start_adventure()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        right_path()

# Start the game
start_adventure()


# In[ ]:




