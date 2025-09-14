#!/usr/bin/env python3
"""
===============================================================================
        = W e l c o m e t o t h e P Y T H O N T U T O R A D V A N C E D =
===============================================================================

    This is a no-bullshit Python tutor ripped off from that VimTutor madness, but
    for Python newbies who think 'print("hello")' is rocket science. Cooked up
    because stock tutorials bore me to tears with their hand-holding crap. Lessons
    1-6: Basics you'll actually use without wanting to kernel-panic. Lesson 7:
    Where we get real—decorators, context managers, and other wizardry that makes
    your code not suck. Edit this file in your editor of choice (vim, duh), fill
    in the blanks as told, save, then run 'python this_file.py' to see if you're
    not a complete idiot. It'll execute everything and spit out results or errors
    (errors mean you fucked up—fix it). Each run starts fresh if you copy from
    original, but experiment or die bored.

    Takes 30-45 mins if you're not spacing out. Make a copy to trash; this one's
    your boot camp. Type the code, run it, feel the burn—or just read like a wimp
    and wonder why your scripts segfault.

    Hit your editor, scroll to Lesson 1.1, edit that shit, save, run from terminal.
    Let's make you not a scripting zombie.

    NOTE: Everything below is commented out. Uncomment sections as you go through
    lessons. Only your uncommented code will run—no spam, just your glorious
    output or spectacular crashes. Uncomment imports, prints, whatever. Start
    with Lesson 1.1: remove the # from the print line and fix it.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    VIM BASIC REVISION: SELECTING TEXT TO WRITE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ** To save part of the file, type v motion :w FILENAME **

  1. Move the cursor to this line.

  2. Press v and move the cursor to the fifth item below. Notice that the
     text is highlighted.

  3. Press the : character. At the bottom of the screen :'<,'> will appear.

  4. Type w TEST , where TEST is a filename that does not exist yet. Verify
     that you see :'<,'>w TEST before you press <ENTER>.

  5. Vim will write the selected lines to the file TEST. Use :!dir or :!ls
     to see it. Do not remove it yet! We will use it in the next lesson.

    NOTE: Pressing v starts Visual selection. You can move the cursor around
    to make the selection bigger or smaller. Then you can use an operator
    to do something with the text. For example, d deletes the text.

    QUICK TIP FOR THIS TUTOR: After uncommenting and editing a lesson's code,
    select just that uncommented block (v, move to cover it), then :w! run.py
    to dump it to run.py. Then :!python run.py to execute it right in Vim.
    See your output or errors without leaving the editor. Efficient, no? Do this
    per lesson—keeps shit isolated, no global fuckups.

"""
# Uncomment and edit as you go—run the file after each lesson to verify.
# Errors? Good, learn from 'em. No errors? You're lying.

# ===== LESSON 1: THE BASICS - SAY HELLO OR GTFO =====

# Lesson 1.1: VARIABLES - STORE YOUR CRAP
# Create a variable 'name' with your name as string, then print "My name is {name}"
# name = 
# print(f"My name is {name}")







# Lesson 1.2: BASIC MATH
# Compute 2 + 2 * 3 / 4 - 1 and print the result (should be 1.5)
# result = 
# print(result)






# Lesson 1.3: STRINGS AND LISTS
# Make a list ['apple', 'banana', 'cherry'], add 'date' to end, print the list
# fruits = ['apple', 'banana', 'cherry']
# 
# print(fruits)








# Lesson 1.4: IF STATEMENTS
# Set age = 25, if age >= 18 print "Adult", else "Kid"
# age = 25
# if :
#     print("Adult")
# else:
#     print("Kid")






# Lesson 1.5: FOR LOOPS
# Loop over [1,2,3,4,5], print each * 2
# for num in [1,2,3,4,5]:
#     print()









# Lesson 1.6: DEFINE A FUNCTION
# Def greet(name): return f"Hello, {name}!"
# Then call greet("Linus") and print it
# def greet(name):
#     return 
# 
# print(greet("Linus"))









# Lesson 1.7: READING FILES
# Write code to open 'test.txt' (create it first with echo "test" > test.txt), read and print content
# But since temp, just simulate: assume content = "Hello file", print it
# with open('test.txt', 'r') as f:
#     content = f.read()
# print(content)









# Lesson 1.8: TRY-EXCEPT
# Try to divide 10/0, catch ZeroDivisionError, print "Can't divide by zero, idiot"
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Can't divide by zero, idiot")









# Lesson 1.9: SIMPLE CLASS
# Class Dog: def __init__(self, name): self.name = name
# def bark(self): print(f"{self.name} says woof!")
# Then dog = Dog("Fido"), dog.bark()
# class Dog:
#     def __init__(self, name):
#         
#     def bark(self):
#         
# 
# dog = Dog("Fido")
# dog.bark()









# Lesson 1.10: DECORATORS - WRAP YOUR FUNCTIONS LIKE A PRO
# Def timer(func): import time; start=time.time(); func(); print(time.time()-start)
# @timer def slow(): time.sleep(1); print("Done")
# slow()
# import time
# def timer(func):
#     def wrapper():
#         
#     return wrapper
# 
# @timer
# def slow():
#     time.sleep(1)
#     print("Done")
# 
# slow()









# Lesson 1.11: GENERATORS - LAZY LISTS, SAVE MEMORY YOU PIG
# Def fib(n): a=0;b=1; while a<n: yield a; a,b = b, a+b
# Then for i in fib(10): print(i)
# def fib(n):
#     
# 
# for i in fib(10):
#     print(i)










# Lesson 1.12: CONTEXT MANAGERS - WITH BLOCKS, CLEANUP AUTOMAGIC
# Class Timer: def __enter__(self): self.start=time.time(); return self
# def __exit__(self, *args): print(time.time()-self.start)
# with Timer(): time.sleep(1); print("Slept")
# class Timer:
#     def __enter__(self):
#         
#     def __exit__(self, *args):
#         
# 
# with Timer():
#     time.sleep(1)
#     print("Slept")

